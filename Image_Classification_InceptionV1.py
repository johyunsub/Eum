import numpy as np
import os
import tensorflow as tf
import tensorflow.contrib.slim as slim

from bs4 import BeautifulSoup as bs
import urllib.request
import requests
import os
import pymysql
import uuid
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import re
from datetime import datetime, timedelta
from PIL import Image
import base64
from io import BytesIO
import time

from nets import inception
from preprocessing import inception_preprocessing

classification_checkpoint_dir = "\\tensorflow-dataset(classification)\\train_inception_v1_dog_FineTune_logs_new\\all"

image_size = inception.inception_v1.default_image_size




juso_db = pymysql.connect(host='j4d103.p.ssafy.io',port=3306,user="ssafy",password="ssafy",db="ieum", cursorclass=pymysql.cursors.DictCursor)

def getanimalnum(pageNum):
    ##다운 받을 주소
    baseUrl = 'https://www.zooseyo.or.kr/Yu_board/freesale_ty_1.html?animal=%EA%B0%95%EC%95%84%EC%A7%80&area=&ty=1&page='   
    url = baseUrl+str(pageNum)  
    req=requests.get(url)
    print(req)
    html = req.text
    soup = bs(html, "html.parser")
    info=soup.select('a[href]')
    checkpoint=False
    ct=0;
    animalnum=[]
    for i in info:
        tags=i.get('href')
        if("sell_up.html?gort=g"==tags):
            ct+=1
        num=tags.split("&")[0].split("?")
        if(ct>1 and num[0]=="view.html"):
            animalnum.append(num[1].split("=")[1])
            
    return animalnum

def getinfo(animalNum):
    preUrl='https://www.zooseyo.or.kr/Yu_board/view.html?no='
    postUrl='&page=1&animal=&area='
    url=preUrl+animalNum+postUrl
    dogsinfo=[]
    
    req=requests.get(url)
    html = req.text
    soup = bs(html, "html.parser")

    #개번호 등록
    dogsinfo.append(animalNum)    
    
    #url 등록
    dogsinfo.append(url)

    
    ##img 경로등록
    imginfo=soup.select('img[src]')
    imglist=[]
    for i in imginfo:
        tags=i.get('src')
        if('/dog_sale/' in tags):
#             print(tags)
            imglist.append('https://www.zooseyo.or.kr'+tags)
    dogsinfo.append(imglist)

    ##개정보 등록
    infos=soup.get_text().split()
    
   ##날짜 인덱스 찾기
    #print(len(infos))
    for i in range(len(infos)):
        try:
            if"무료분양" in infos[i]:
                dogsinfo.append(infos[i].split("(")[1])
                break
        except:
            dogsinfo.append("")
    

    for idx in [356,364,366,368]:
        dogsinfo.append(infos[idx])
    
    return dogsinfo

def saveimg(directory,url):    
    urls=url.split("/")
    extension=urls[len(urls)-1].split(".")[1]
    date=datetime.today()
    month=int(datetime.today().month/10)*10+int(datetime.today().month%10)
    day=int(datetime.today().day/10)*10+int(datetime.today().day%10)
    path1=str(datetime.today().year)+str(month)+ str(day)
    
    n=1
    imguuid=uuid.uuid1();
    save_path= directory+"/"+path1
    save_root = directory+"/"+path1
    if not os.path.exists(save_root):os.makedirs(save_root)
    try:
        with urlopen(url) as f:
            with open(os.path.join(save_path, str(imguuid)+"."+extension),'wb') as h: # w - write b - binary
                img = f.read()
                h.write(img)
        print(f"directory :  {save_path}  파일명 : {imguuid} 원본 파일명 : {urls[len(urls)-1]}")
    except:
        print("error")
    return [save_path,str(imguuid)+"."+extension,"",extension,urls[len(urls)-1]]
    
def predict(path):
	result=[]
	img = path[0]
	
	with tf.Graph().as_default():
	   image_input = tf.read_file(img)
	   image = tf.image.decode_jpeg(image_input, channels=3)
	   processed_image = inception_preprocessing.preprocess_image(image, image_size, image_size, is_training=False)

	   processed_images = tf.expand_dims(processed_image, 0)

	   with slim.arg_scope(inception.inception_v1_arg_scope()):
	      logits, _ = inception.inception_v1(processed_images, num_classes=135, is_training=False)
	   probabilities = tf.nn.softmax(logits)

	   init_fn = slim.assign_from_checkpoint_fn(os.path.join(classification_checkpoint_dir, 'model.ckpt-500'), slim.get_model_variables('InceptionV1'))

	   config = tf.ConfigProto()
	   config.gpu_options.allow_growth = True
	   with tf.Session(config = config) as sess:
	      init_fn(sess)
	      np_image, probabilities = sess.run([image, probabilities])
	      probabilities = probabilities[0, 0:]
	      sorted_inds = [i[0] for i in sorted(enumerate(-probabilities), key=lambda x:x[1])]

	   names = os.listdir("\\tensorflow-dataset(classification)\\dogs_new\\dog_photos")
	   
	   for i in range(3):
	      index = sorted_inds[i]
	      name = names[index]

	      if name == '1043-n000001-Shiba_Dog':
		      name = "시바"
	      elif name == '1121-n000002-French_bulldog':
	          name = "불독"
	      elif name == '1160-n000003-Siberian_husky':
		      name = "시베리안 허스키"
	      elif name == '1324-n000004-malamute':
		      name = "알래스카 말라뮤트"
	      elif name == '1936-n000005-Pomeranian':
		      name = "포메라니안"
	      elif name == '200-n000008-Airedale':
		      name = "에어데일 테리어"
	      elif name == '200-n000010-miniature_poodle':
		      name = "푸들"
	      elif name == '200-n000012-affenpinscher':
		      name = "아펜핀셔"
	      elif name == '201-n000024-schipperke':
		      name = "스키퍼키"
	      elif name == '202-n000020-Australian_terrier':
		      name = "오스트레일리안 테리어"
	      elif name == '202-n000023-Welsh_springer_spaniel':
		      name = "웰시 스프링거 스파니엘"
	      elif name == '202-n000028-curly_coated_retriever':
		      name = "컬리 코티드 리트리버"
	      elif name == '203-n000015-Staffordshire_bullterrier':
		      name = "스타포드셔 불테리어"
	      elif name == '203-n000016-Norwich_terrier':
		      name = "노리치 테리어"
	      elif name == '203-n000021-Tibetan_terrier':
		      name = "티베탄 테리어"
	      elif name == '203-n000022-English_setter':
		      name = "잉글리시 세터"
	      elif name == '203-n000027-Norfolk_terrier':
		      name = "노퍽 테리어"
	      elif name == '205-n000029-Pembroke':
		      name = "웰시코기"
	      elif name == '205-n000030-Tibetan_mastiff':
		      name = "티베탄 마스티프"
	      elif name == '206-n000007-Border_terrier':
		      name = "보더 테리어"
	      elif name == '206-n000035-Great_Dane':
		      name = "그레이트 데인"
	      elif name == '206-n000037-Scotch_terrier':
		      name = "스코티시 테리어"
	      elif name == '206-n000047-flat_coated_retriever':
		      name = "플랫 코티드 리트리버"
	      elif name == '206-n000051-Saluki':
		      name = "살루키"
	      elif name == '207-n000011-Irish_setter':
		      name = "아이리시 세터"
	      elif name == '207-n000026-Blenheim_spaniel':
		      name = "킹 찰스 스파니엘"
	      elif name == '207-n000036-Irish_terrier':
		      name = "아이리시 테리어"
	      elif name == '207-n000044-bloodhound':
		      name = "블러드 하운드"
	      elif name == '207-n000045-redbone':
		      name = "레드본 쿤하운드"
	      elif name == '209-n000040-West_Highland_white_terrier':
		      name = "웨스트 하일랜드 화이트 테리어"
	      elif name == '209-n000042-Brabancon_griffo':
		      name = "브뤼셀 그리펀"
	      elif name == '209-n000043-dhole':
		      name = "승냥이"
	      elif name == '209-n000049-kelpie':
		      name = "오스트레일리안 켈피"
	      elif name == '209-n000054-Doberman':
		      name = "도베르만"
	      elif name == '210-n000006-Ibizan_hound':
		      name = "이비전 하운드"
	      elif name == '210-n000048-vizsla':
		      name = "비즐라"
	      elif name == '211-n000009-cairn':
		      name = "케언 테리어"
	      elif name == '211-n000018-German_shepherd':
		      name = "져먼 셰퍼드"
	      elif name == '211-n000025-African_hunting_dog':
		      name = "아프리카 들개"
	      elif name == '211-n000052-Dandie_Dinmont':
		      name = "댄디 딘몬트 테리어"
	      elif name == '211-n000058-Sealyham_terrier':
		      name = "실리엄 테리어"
	      elif name == '211-n000059-German_short_haired_pointer':
		      name = "저먼 쇼트헤어드 포인터"
	      elif name == '211-n000061-Bernese_mountain_dog':
		      name = "버니즈 마운틴 도그"
	      elif name == '211-n000068-Saint_Bernard':
		      name = "세인트 버나드"
	      elif name == '214-n000019-Leonberg':
		      name = "레온버르거"
	      elif name == '214-n000033-Bedlington_terrier':
		      name = "베들링턴 테리어"
	      elif name == '215-n000031-Newfoundland':
		      name = "뉴펀들랜드 도그"
	      elif name == '215-n000038-Lhasa':
		      name = "라사압소"
	      elif name == '215-n000075-Chesapeake_Bay_retriever':
		      name = "체서피크 베이 리트리버"
	      elif name == '216-n000017-Lakeland_terrier':
		      name = "레이클랜드 테리어"
	      elif name == '216-n000063-Walker_hound':
		      name = "워커 하운드"
	      elif name == '216-n000078-American_Staffordshire_terrier':
		      name = "아메리칸 스타포드셔 불테리어"
	      elif name == '217-n000014-otterhound':
		      name = "오터 하운드"
	      elif name == '217-n000034-Sussex_spaniel':
		      name = "서식스 스파니엘"
	      elif name == '217-n000046-Norwegian_elkhound':
		      name = "노르웨이언 엘크하운드"
	      elif name == '217-n000050-bluetick':
		      name = "블루틱 쿤하운드"
	      elif name == '217-n000079-dingo':
		      name = "딩고 도그"
	      elif name == '219-n000066-Irish_water_spaniel':
		      name = "아이리시 워터 스파니엘"
	      elif name == '2192-n000088-Samoyed':
		      name = "사모예드"
	      elif name == '220-n000032-Fila Braziliero':
		      name = "필라 브라질레이로"
	      elif name == '220-n000053-standard_schnauzer':
		      name = "스탠다드 슈나우저"
	      elif name == '220-n000069-Mexican_hairless':
		      name = "멕시칸 헤어리스 도그"
	      elif name == '221-n000055-EntleBucher':
		      name = "엔틀버쳐 마운틴 도그"
	      elif name == '222-n000013-Afghan_hound':
		      name = "아프간 하운드"
	      elif name == '223-n000067-kuvasz':
		      name = "쿠바츠"
	      elif name == '223-n000074-English_foxhound':
		      name = "잉글리시 폭스하운드"
	      elif name == '223-n000092-keeshond':
		      name = "키스혼드"
	      elif name == '224-n000039-Irish_wolfhound':
		      name = "아이리시 울프하운드"
	      elif name == '224-n000056-Scottish_deerhound':
		      name = "스코티시 디어하운드"
	      elif name == '224-n000060-Rottweiler':
		      name = "로트와일러"
	      elif name == '225-n000062-black_and_tan_coonhound':
		      name = "블랙 앤 탄 쿤하운드"
	      elif name == '225-n000073-Great_Pyrenees':
		      name = "그레이트 피레니즈"
	      elif name == '225-n000082-boxer':
		      name = "복서"
	      elif name == '226-n000057-wire_haired_fox_terrier':
		      name = "와이어 폭스 테리어"
	      elif name == '226-n000064-borzoi':
		      name = "보르조이"
	      elif name == '227-n000070-groenendael':
		      name = "그루넨달"
	      elif name == '227-n000094-collie':
		      name = "콜리"
	      elif name == '228-n000085-Gordon_setter':
		      name = "고든 세터"
	      elif name == '229-n000087-Kerry_blue_terrier':
		      name = "케리 블루 테리어"
	      elif name == '230-n000041-briard':
		      name = "브리아드"
	      elif name == '230-n000080-Rhodesian_ridgeback':
		      name = "로디지안 리지백"
	      elif name == '230-n000084-Boston_bull':
		      name = "보스턴 테리어"
	      elif name == '231-n000077-bull_mastiff':
		      name = "불 마스티프"
	      elif name == '231-n000081-silky_terrier':
		      name = "실키 테리어"
	      elif name == '232-n000076-Brittany_spaniel':
		      name = "브리트니 스파니엘"
	      elif name == '232-n000083-Eskimo_dog':
		      name = "에스키모 도그"
	      elif name == '232-n000089-giant_schnauzer':
		      name = "자이언트 슈나우저"
	      elif name == '233-n000071-malinois':
		      name = "벨지안 셰퍼드"
	      elif name == '233-n000072-Bouvier_des_Flandres':
		      name = "부비에 데 플랑드르"
	      elif name == '234-n000065-whippet':
		      name = "휘핏"
	      elif name == '234-n000091-Appenzeller':
		      name = "아펜젤러 세넨훈드"
	      elif name == '234-n000093-Chinese_Crested_Dog':
		      name = "차이니스 크레스티드 도그"
	      elif name == '2342-n000102-miniature_schnauzer':
		      name = "미니어처 슈나우저"
	      elif name == '235-n000090-soft_coated_wheaten_terrier':
		      name = "아이리시 소프트코티드 휘튼 테리어"
	      elif name == '235-n000096-Weimaraner':
		      name = "와이머라너"
	      elif name == '235-n000097-clumber':
		      name = "클럼버 스파니엘"
	      elif name == '237-n000086-Greater_Swiss_Mountain_dog':
		      name = "그레이터 스위스 마운틴 도그"
	      elif name == '237-n000095-toy_terrier':
		      name = "토이 테리어"
	      elif name == '238-n000099-Italian_greyhound':
		      name = "이탈리안 그레이하운드"
	      elif name == '241-n000100-basset':
		      name = "바셋 하운드"
	      elif name == '243-n000103-basenji':
		      name = "바센지"
	      elif name == '245-n000098-Australian_Shepherd':
		      name = "오스트레일리안 셰퍼드"
	      elif name == '249-n000101-Maltese_dog':
		      name = "말티즈"
	      elif name == '249-n000106-Japanese_spaniel':
		      name = "재패니즈 스파니엘"
	      elif name == '253-n000105-Cane_Carso':
		      name = "카네코르소"
	      elif name == '253-n000107-Japanese_Spitzes':
		      name = "재패니즈 스피츠"
	      elif name == '257-n000108-Old_English_sheepdog':
		      name = "올드 잉글리시 쉽독"
	      elif name == '258-n000104-Black_sable':
		      name = "셰퍼드"
	      elif name == '2594-n000109-Border_collie':
		      name = "보더콜리"
	      elif name == '274-n000110-Shetland_sheepdog':
		      name = "셔틀랜드 쉽독"
	      elif name == '276-n000112-English_springer':
		      name = "잉글리시 스프링거"
	      elif name == '276-n000113-beagle':
		      name = "비글"
	      elif name == '286-n000111-cocker_spaniel':
		      name = "코카 스파니엘"
	      elif name == '2909-n000116-Cardigan':
		      name = "웰시코기"
	      elif name == '2925-n000114-toy_poodle':
		      name = "푸들"
	      elif name == '3083-n000117-Bichon_Frise':
		      name = "비숑"
	      elif name == '316-n000118-standard_poodle':
		      name = "푸들"
	      elif name == '318-n000115-komondor':
		      name = "코몬도르"
	      elif name == '329-n000119-chow':
		      name = "차우차우"
	      elif name == '340-n000120-Yorkshire_terrier':
		      name = "요크셔테리어"
	      elif name == '3580-n000122-Labrador_retriever':
		      name = "래브라도 리트리버"
	      elif name == '361-n000123-Shih_Tzu':
		      name = "시츄"
	      elif name == '420-n000124-Chihuahua':
		      name = "치와와"
	      elif name == '480-n000125-Pekinese':
		      name = "페키니즈"
	      elif name == '5355-n000126-golden_retriever':
		      name = "골든리트리버"
	      elif name == '561-n000127-miniature_pinscher':
		      name = "미니어처 핀셔"
	      elif name == '7449-n000128-teddy':
		      name = "푸들"
	      elif name == '7500-n000130-Yellow_Jindo':
		      name = "진도"
	      elif name == '7501-n000131-White_Jindo':
		      name = "진도"
	      elif name == '7502-n000132-Black_Jindo':
		      name = "진도"
	      elif name == '7503-n000133-Tiger_Jindo':
		      name = "진도"
	      elif name == '7504-n000134-Black_tan_Jindo':
		      name = "진도"
	      elif name == '7505-n000135-Blend_Jindo':
		      name = "진도"
	      elif name == '798-n000130-pug':
		      name = "퍼그"
	      elif name == '806-n000129-papillon':
		      name = "파피용"


	      result.append(name)
	      result.append(probabilities[index]*100)

	print(result)
	return result


def saveAndInsert(dogInfos):
    dognum=info[0]
    detailurl=info[1]
    imgurls=info[2]
    date=info[3].split(".")
    date=date[0]+"-"+date[1]+"-"+date[2]
    breed=info[4]
    location=info[5]
    sex=info[6]
    phoneNumRegex = re.compile(r'\d{3}-\d{4}-\d{4}')
    phone=phoneNumRegex.findall(info[7])
    if phone==[]:
        phone=""
    else:
        phone=phone[0]
        
    ismixed=False
    
    cursor = juso_db.cursor()
    
    #######################파일 저장############################
    #server
    #dir="/home/upload/img"
    #local    
    dir="D://pjt2"
    orginnamelist=[]
    systemimgpaths=[]
    #predictlst=[]
    try:        
        for i in range(1,len(imgurls)):
            saveresult=saveimg(dir,imgurls[i])

            image_path = saveresult[0]+"/"+saveresult[1]
            
            with open(image_path,"rb") as image_file:
            	binary_image = image_file.read()

            binary_image = base64.b64encode(binary_image)
            #binary_image = binary_image.decode('UTF-8')

            sql="INSERT INTO `ieum`.`file`(`size`,`type`,`image`,`origin_name`) "+\
            f"VALUES('0','{saveresult[3]}','{binary_image}','{saveresult[4]}'); "

            cursor.execute(sql)
            result = cursor.fetchall()
            juso_db.commit()        
            print(saveresult[0]+"/"+saveresult[1])
            orginnamelist.append(saveresult[4])
            systemimgpaths.append(image_path)
        print(breed)
        print("file insert  done")
    except Exception  as e:
        print("file insert error",e)
        
    
    if "믹스" in breed:
        ismixed=True
        #ex [(predict_breed,percent)]
        predictlst=predict(systemimgpaths)
        breed = predictlst[0]
        maxpercent = predictlst[1]
        
        
    #####################insert doginfo table##########################
    try:

        sql = "INSERT INTO `ieum`.`doginfo`(`id`,`breed`,`location`,`url`,`phone`,`datetime`,`sex`)"+\
        f" VALUES('{dognum}','{breed}','{location}','{detailurl}','{phone}','{date}','{sex}'); "

        cursor.execute(sql)
        result = cursor.fetchall()
        juso_db.commit()        
        print("doginfo insert done")
    except Exception  as e:
        print("doginfo insert error",e)
        return 

    #####################insert doginfoimages table##########################
    
    try:
        for orginname in orginnamelist:
            sql = f"SELECT id FROM `ieum`.`file` WHERE origin_name='{orginname}' ;"
            cursor.execute(sql)
            fileId = cursor.fetchall()
            print("fileId ",fileId[0]['id'])
            sql="INSERT INTO `ieum`.`doginfoimage`(`dogid`,`file_id`)" + \
            f" VALUES('{dognum}','{fileId[0]['id']}'); "
            cursor.execute(sql)
            fileId = cursor.fetchall()
        print("doginfoimages insert  done")
    except Exception  as e:
        print("doginfoimages insert  done",e)
        
    ####################insert doginfopredict table##########################
    
    if ismixed==False :
        return 
    
    try:
        sql="INSERT INTO `ieum`.`doginfopredict`(`dogid`,`percent`,`predicted_breed`) "+ \
        f"VALUES('{dognum}','{predictlst[1]}','{predictlst[0]}'); "
        cursor.execute(sql)
        fileId = cursor.fetchall()
        sql="INSERT INTO `ieum`.`doginfopredict`(`dogid`,`percent`,`predicted_breed`) "+ \
        f"VALUES('{dognum}','{predictlst[3]}','{predictlst[2]}'); "
        cursor.execute(sql)
        fileId = cursor.fetchall()
        sql="INSERT INTO `ieum`.`doginfopredict`(`dogid`,`percent`,`predicted_breed`) "+ \
        f"VALUES('{dognum}','{predictlst[5]}','{predictlst[4]}'); "
        cursor.execute(sql)
        fileId = cursor.fetchall()
        print("doginfopredict insert  done")
    except Exception  as e:
        print("doginfopredict insert  done",e)
    
    
    


date=datetime.today()
month=int(datetime.today().month/10)*10+int(datetime.today().month%10)
day=int(datetime.today().day/10)*10+int(datetime.today().day%10)
endDate=str(datetime.today().year)+str(month)+ str(day)       

if __name__ == "__main__":
    
    #크롤링 멈추는 날짜(등록일 기준)
    date=datetime.today() - timedelta(1)
    month=str(int((datetime.today() - timedelta(1)).month/10)*10)+str((datetime.today() - timedelta(1)).month%10)
    day=int((datetime.today() - timedelta(1)).day/10)*10+int((datetime.today() - timedelta(1)).day%10)
    endDate=str((datetime.today() - timedelta(1)).year)+"."+str(month) +"."+str(day)
    print("crawling :",endDate)
    ##if you want 
    
    end = time.strptime(endDate, "%Y.%m.%d")

    dogInfos=[]
    ##넘겨볼 페이지 갯수
    for pageNum in range(0,4):
        animalNums=getanimalnum(pageNum)
        cnt=0
        for num in animalNums:
            cnt+=1
            info=getinfo(num)
            
            tmp = time.strptime(info[len(info)-5], "%Y.%m.%d")

            if(tmp < end):
            	break
            #print("====개정보===")
            #print("pageNum : ",pageNum,info)
            #print(info[len(info)-5])            
            dogInfos.append(info)

    for info in dogInfos:
    	saveAndInsert(info)


'''
with tf.Graph().as_default():

   #start = time.time()

   image_input = tf.read_file("\\tensorflow-dataset(classification)\\test images\\dogs\\5.jpg")
   image = tf.image.decode_jpeg(image_input, channels=3)
   processed_image = inception_preprocessing.preprocess_image(image, image_size, image_size, is_training=False)

   processed_images = tf.expand_dims(processed_image, 0)

   with slim.arg_scope(inception.inception_v1_arg_scope()):
      logits, _ = inception.inception_v1(processed_images, num_classes=135, is_training=False)
   probabilities = tf.nn.softmax(logits)

   init_fn = slim.assign_from_checkpoint_fn(os.path.join(classification_checkpoint_dir, 'model.ckpt-500'), slim.get_model_variables('InceptionV1'))

   config = tf.ConfigProto()
   config.gpu_options.allow_growth = True
   with tf.Session(config = config) as sess:
      init_fn(sess)
      np_image, probabilities = sess.run([image, probabilities])
      probabilities = probabilities[0, 0:]
      sorted_inds = [i[0] for i in sorted(enumerate(-probabilities), key=lambda x:x[1])]

   #plt.figure()
   #plt.imshow(np_image.astype(np.uint8))
   #plt.axis('off')
   #plt.show()

   names = os.listdir("\\tensorflow-dataset(classification)\\dogs_new\\dog_photos")
   #line = ""
   
   for i in range(3):
      index = sorted_inds[i]
      line = 'Probability %0.2f%% => [%s]' % (probabilities[index], names[index])
      print(line)
'''
   #give(line)

   #print(time.time() - start)
   