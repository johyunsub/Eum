# 이음 : classification을 통해 쉽고 편하게 나에게 맞는 유기견 입양을 도와주는 서비스 
## 역할 
### 프론트 : 조현섭, 지승윤, 이수민
### 백엔드 : 김성실
### 인공지능 : 지서연

## code 
### Requirements
> * Node Package Module
> * MySQL
> * Python 3.6
> * JDK 1.8

## install

```bash
$ git https://lab.ssafy.com/s04-ai-speech-sub3/s04p23d103.git
```

```bash
$ yarn install
```

### 1.database

> ###### ieum.sql을 참조 하여 데이터 베이스 생성 
 
### 2.backend server run
> ###### application.yml 에서 database 설정 변경
> ###### 빌드 & 실행
```bash
$ ./gradlew build
$ java -jar [filename].jar
```
### 3.frontserver server run
> ###### backend server 에 맞춰 api 요청 주소 변경

```bash
$ yarn run serve
```

***          
## classification dataset

> ###### stanford dogs dataset 과 Tsinghua dogs dataset 에서 사진을 선별하고 진돗개 이미지를 추가해 135개의 개 종류에 대해 68,569 장의 이미지를 가진 전용 데이터셋을 만듬 

## classification 학습 모델 

> ###### ImageNet으로 pre-trained 된 Inception V1 모델을 사용