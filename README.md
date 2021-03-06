> SSAFY Team 3 
>
> ์ธ๊ณต์ง๋ฅ PTJ

# ๐ถ ์ด์ (Eum)



<img width="20%" src="https://user-images.githubusercontent.com/42338624/116283738-3259ab80-a7c7-11eb-9d47-19309641f75b.png" alt="logo" />

------


#### | ์ด์ :: MDTI(MyDogTypeIndecator)๋ก ์ฌ์ฉ์์ ์ฑํฅ์ ๋ง๋ ๋ฐ๋ ค๊ฒฌ์ ์ถ์ฒํ๊ณ  Classification์ ํตํด ์ ๊ธฐ๊ฒฌ์ ํ์ข์ ์์ํ  ์ ์๊ฒํ๊ณ  ์์์ ๋์์ฃผ๋ ์๋น์ค ๐โ๐ฆบ




![์์ฐ์์](https://user-images.githubusercontent.com/42338624/116279757-e1e04f00-a7c2-11eb-9abc-fd19db5f0e4c.gif)








<br />

## ๐ง Architecture

**Entitiy Relationship Diagram**

<img width="80%" src="./์ฐ์ถ๋ฌผ/ERD.png" />

<br />

**Sequence Diagrams**

<img width="80%" src="./์ฐ์ถ๋ฌผ/์ด์_์ํ์ค๋ค์ด์ด๊ทธ๋จ.png" />


------




<br />

### ๐ฆ Requirements
> * Node Package Module
> * MySQL
> * Python 3.6
> * JDK 1.8




<br />

## ๐ install

```bash
$ git https://lab.ssafy.com/s04-ai-speech-sub3/s04p23d103.git
```

```bash
$ yarn install
```


### 1. database

> ###### ieum.sql์ ์ฐธ์กฐ ํ์ฌ ๋ฐ์ดํฐ ๋ฒ ์ด์ค ์์ฑ 


### 2. backend server run
> ###### application.yml ์์ database ์ค์  ๋ณ๊ฒฝ
> ###### ๋น๋ & ์คํ
```bash
$ ./gradlew build
$ java -jar [filename].jar
```


### 3. frontserver server run
> ###### backend server ์ ๋ง์ถฐ api ์์ฒญ ์ฃผ์ ๋ณ๊ฒฝ

```bash
$ yarn run serve
```



<br />

## ๐ฌ classification dataset

> ###### stanford dogs dataset ๊ณผ Tsinghua dogs dataset ์์ ์ฌ์ง์ ์ ๋ณํ๊ณ  ์ง๋๊ฐ ์ด๋ฏธ์ง๋ฅผ ์ถ๊ฐํด 135๊ฐ์ ๊ฐ ์ข๋ฅ์ ๋ํด 68,569 ์ฅ์ ์ด๋ฏธ์ง๋ฅผ ๊ฐ์ง ์ ์ฉ ๋ฐ์ดํฐ์์ ๋ง๋ฌ 

### ๐งฌclassification ํ์ต ๋ชจ๋ธ 

> ###### ImageNet์ผ๋ก pre-trained ๋ Inception V1 ๋ชจ๋ธ์ ์ฌ์ฉ





------





<br />



<br />

## ๐ MDTI Solution

> MDTI(My Dog Type  Indicator)๊ฒ์ฌ์ ์ฑ์ ๋ฐฉ์์ ์ด๋ป๊ฒ ์ฒ๋ฆฌํ์๋ ์ง์ ๋ํ ์ค๋ช์๋๋ค.



### ๐ MDTI Questionnaire

> MDTI๊ฒ์ฌ์ ์ง๋ฌธ๊ณผ ์ ํ์ง๋ฅผ ํ๋ก ๋ํ๋ด์์ ๋์ ๊ตฌํํ ์ฝ๋์๋๋ค.

| Question No. |                ์ง๋ฌธ                | ์ ํ์ง                                                       | Key             |
| :----------: | :--------------------------------: | :----------------------------------------------------------- | :-------------- |
|      Q1      |       ๋ฐ๋ ค๊ฒฌ์ ํธ์ด ๋น ์ง๋ค๋ฉด       | โ  ์๊ด์๋ค<br />โก ์ด๋ ์ ๋ ๊ด์ฐฎ๋ค<br />โข ์๋ฏผํ๋ค           | O<br />O<br />X |
|      Q2      | ํจ๊ป ์ด๊ธฐ์ ์ ๋นํ ๋ฐ๋ ค๊ฒฌ์ ํฌ๊ธฐ๋ | โ  5kg ์ดํ ์ํ๊ฒฌ<br />โก 10kg ์ํ์ ์คํ๊ฒฌ<br />โข 15kg ์ด์ ๋ํ๊ฒฌ | X<br />X<br />O |
|      Q3      |     ํ๋ฃจ์ ์ฐ์ฑ ๊ฐ๋ฅํ ์๊ฐ์      | โ  ์ง ์ฃผ๋ณ์์ ๊ฐ๋ฒผ์ด ์ฐ์ฑ<br />โก 2์๊ฐ ์ด์ ์ฐ์ฑ             | O<br />X        |
|      Q4      |    ์ฐ๋ฆฌ์ง ๋ฐ๋ ค๊ฒฌ์ด ์ง๋ ์ ๋๋     | โ  ๋ง์ด ์ง์ง ์์์ผ๋ฉด ์ข๊ฒ ๋ค<br />โก ์ง์ ํ๋ จ์ผ๋ก ๊ทน๋ณต ๊ฐ๋ฅํ๋ค | X<br />O        |
|      Q5      |     ๊ฐ์กฑ์ด ์ง์ ๋น์ฐ๋ ๊ฒฝ์ฐ๋      | โ  ๊ฐ์กฑ์ด ์ง์ ์๋ ๊ฒฝ์ฐ๊ฐ ๋ง๋ค<br />โก ๋๋๋ก ๋ชจ๋ ์ง์ ๋น์ด๋ค | X<br />O        |
|      Q6      |   ํค์ฐ๊ณ  ์ถ์ ๋ฐ๋ ค๊ฒฌ์ ์ด๋ฏธ์ง๋    | โ  ์ธ๊ธฐ ๋ง์ ํ์ข ์ค ํ๋์์ผ๋ฉด<br />โก ๋ด๊ฐ ์ข๋ค๋ฉด ์๋ฌด๋๋ ์๊ด์๋ค | O<br />X        |

```javascript
 questions: [ 	//question: ์ง๋ฌธ; no: QuestionNo; props: ์ ํ์ง; correct: Key; accuracy: ์ ํ๋ 
            {
              question: "๋ฐ๋ ค๊ฒฌ์ ํธ์ด ๋น ์ง๋ค๋ฉด...",
              propositions: [
                { no: 11, props: "์๊ด์๋ค", correct: true, accuracy: 0.93 },
                { no: 12, props: "์ด๋ ์ ๋ ๊ด์ฐฎ๋ค", correct: true, accuracy: 0.81 },
                { no: 13, props: "์๋ฏผํ๋ค", correct: false, accuracy: 0.93 },
              ],
              solved: false,
            },
            {
              question: "ํจ๊ป ์ด๊ธฐ์ ์ ๋นํ ๋ฐ๋ ค๊ฒฌ์ ํฌ๊ธฐ๋...",
              propositions: [
                { no: 21, props: "5kg ์ดํ ์ํ๊ฒฌ", correct: false, accuracy: 0.93},
                { no: 22, props: "10kg ์ํ์ ์คํ๊ฒฌ", correct: false, accuracy: 0.71},
                { no: 23, props: "15kg ์ด์ ๋ํ๊ฒฌ", correct: true, accuracy: 0.93},
              ],
              solved: false,
            },
            {
              question: "ํ๋ฃจ์ ์ฐ์ฑ ๊ฐ๋ฅํ ์๊ฐ์...",
              propositions: [
                { no: 31, props: "์ง ์ฃผ๋ณ์์ ๊ฐ๋ฒผ์ด ์ฐ์ฑ", correct: true, accuracy: 0.93 },
                { no: 32, props: "2์๊ฐ ์ด์ ์ฐ์ฑ", correct: false, accuracy: 0.93 },
              ],
              solved: false,
            },
            {
              question: "์ฐ๋ฆฌ์ง ๋ฐ๋ ค๊ฒฌ์ด ์ง๋ ์ ๋๋...",
              propositions: [
                { no: 41, props: "๋ง์ด ์ง์ง ์์์ผ๋ฉด ์ข๊ฒ ๋ค", correct: false, accuracy: 0.93,},
                { no: 42, props: "์ง์ ํ๋ จ์ผ๋ก ๊ทน๋ณต ๊ฐ๋ฅํ๋ค", correct: true, accuracy: 0.93, },
              ],
              solved: false,
            },
            {
              question: "๊ฐ์กฑ์ด ์ง์ ๋น์ฐ๋ ๊ฒฝ์ฐ๋...",
              propositions: [
                { no: 51, props: "๊ฐ์กฑ์ด ์ง์ ์๋ ๊ฒฝ์ฐ๊ฐ ๋ง๋ค.", correct: false, accuracy: 0.93, },
                { no: 52, props: "๋๋๋ก ๋ชจ๋ ์ง์ ๋น์ด๋ค.", correct: true, accuracy: 0.55 },
              ],
              solved: false,
            },
            {
              question: "ํค์ฐ๊ณ  ์ถ์ ๋ฐ๋ ค๊ฒฌ์ ์ด๋ฏธ์ง๋...",
              propositions: [
                { no: 61, props: "์ธ๊ธฐ ๋ง์ ํ์ข ์ค ํ๋์์ผ๋ฉด", correct: true, accuracy: 0.93, },
                { no: 62, props: "๋ด๊ฐ ์ข๋ค๋ฉด ์๋ฌด๋๋ ์๊ด์๋ค.", correct: false, accuracy: 0.93, },
              ],
              solved: false,
            },
          ],
```




<br />

### ๐ถ ํ์ข๋ณ Question's Key

> ํ์ข์ ๋ฐ๋ผ ์ง๋ฌธ์ ํด๋น๋๋ key๊ฐ
>
> ex) ๋น์์ ์ ํฉํ ๊ฒฌ์ฃผ๋ ํธ๋น ์ง์ ์๋ฏผํ๋ฉฐ, ์ํ๊ฒฌ์ ์ ํธํ๊ณ , ๊ฐ๋ฒผ์ด ์ฐ์ฑ์ ์ฆ๊ธฐ๋ฉฐ, ๋ง์ด ์ง์ง์์ผ๋ฉฐ, ์ง์ ์๋ ์๊ฐ์ด ๋ง๊ณ , ์ธ๊ธฐ์๋ ํ์ข์ ์ ํธํ๋ ์ฌ๋์ ํด๋น๋  ๊ฒ์๋๋ค. ๋ฐ๋ผ์ ๋ค์ ํ์ ๊ฐ์ ๊ฐ์ ๊ฐ์ง๊ฒ ๋ฉ๋๋ค.

|                  |  Q1  |  Q2  |  Q3  |  Q4  |  Q5  |  Q6  |
| :--------------: | :--: | :--: | :--: | :--: | :--: | :--: |
|     **๋น์**     |  X   |  X   |  O   |  X   |  X   |  O   |
|     **์์ธ**     |  O   |  X   |  O   |  X   |  O   |  X   |
| **๊ณจ๋ ๋ฆฌํธ๋ฆฌ๋ฒ** |  O   |  O   |  X   |  O   |  O   |  O   |
| **์ํฌ์ํ๋ฆฌ์ด** |  X   |  O   |  O   |  X   |  O   |  X   |
|   **์ฐ์์ฝ๊ธฐ**   |  X   |  X   |  O   |  X   |  O   |  O   |
|    **๋งํฐ์ฆ**    |  O   |  X   |  O   |  O   |  X   |  X   |
|     **ํธ๋ค**     |  X   |  X   |  O   |  O   |  X   |  O   |
|     **๋ถ๋**     |  X   |  O   |  O   |  X   |  O   |  O   |
|  **ํฌ๋ฉ๋ผ๋์**  |  O   |  X   |  O   |  O   |  X   |  O   |
|   **๋ณด๋์ฝ๋ฆฌ**   |  O   |  O   |  X   |  X   |  O   |  X   |
|     **์๋ฐ**     |  X   |  X   |  X   |  X   |  O   |  O   |
|     **์ง๋**     |  X   |  X   |  X   |  O   |  O   |  X   |
|    **์น์์**    |  X   |  X   |  O   |  O   |  X   |  X   |

```javascript
dogsMdti: [     //MDTI์์ ํ์ฉ๋๋ ํ์ข์๋ฐ๋ฅธ ์ง๋ฌธ์๋ฐ๋ฅธ ๋ต(Answer the Question)
            {breed: "๋น์", AtQ: [false, false, true, false, false, true] },
            {breed: "์์ธ", AtQ: [true, false, true, false, true, false] },
            {breed: "๊ณจ๋ ๋ฆฌํธ๋ฆฌ๋ฒ", AtQ: [true, true, false, true, true, true] },
            {breed: "์ํฌ์ํ๋ฆฌ์ด", AtQ: [false, true, true, false, true, false] },
            {breed: "์ฐ์์ฝ๊ธฐ", AtQ: [false, false, true, false, true, true] },
            {breed: "๋งํฐ์ฆ", AtQ: [true, false, true, true, false, false] },
            {breed: "ํธ๋ค", AtQ: [false, false, true, true, false, true] },
            {breed: "๋ถ๋", AtQ: [false, true, true, false, true, true] },
            {breed: "ํฌ๋ฉ๋ผ๋์", AtQ: [true, false, true, true, false, true] },
            {breed: "๋ณด๋์ฝ๋ฆฌ", AtQ: [true, true, false, false, true, false] },
            {breed: "์๋ฐ", AtQ: [false, false, false, false, true, true] },
            {breed: "์ง๋", AtQ: [false, false, false, true, true, false] },
            {breed: "์น์์", AtQ: [false, false, true, true, false, false] },
        ],
```




<br />

### ๐ ScoreBoard

> ํ์ข์ ๋ฐ๋ผ ์ ์๋ฅผ ๋งค๊ธธ ์ ์๋ ์ ์ํ์๋๋ค. ์ ์๊ฐ ๊ฐ์ฅ ๋์ ์๋ก ์ค๋ฌธ์์ ์ ํฉํ ํ์ข์๋๋ค.

|           | ๋น์ | ์์ธ | ๊ณจ๋ ๋ฆฌํธ๋ฆฌ๋ฒ | ์ํฌ์ํ๋ฆฌ์ด | ์ฐ์์ฝ๊ธฐ | ๋งํฐ์ฆ | ํธ๋ค | ๋ถ๋ | ํฌ๋ฉ๋ผ๋์ | ๋ณด๋์ฝ๋ฆฌ | ์๋ฐ | ์ง๋ | ์น์์ |
| :-------: | :--: | :--: | :----------: | :----------: | :------: | :----: | :--: | :--: | :--------: | :------: | :--: | :--: | :----: |
| **score** |  0   |  0   |      0       |      0       |    0     |   0    |  0   |  0   |     0      |    0     |  0   |  0   |   0    |

```javascript
mdtiScoreboard: [   //MDTI์์ ์์ฑ๋ ์ค๋ฌธ์ ๋ฐํ์ผ๋ก ์ ์ ์ ๊ฐ์ฅ ๋ง๋ ๊ฐ์์ง๋ฅผ ์ถ์ฒํด์ฃผ๊ธฐ์ํ ์ ์ํ
          {breed: "๋น์", score: 0},
          {breed: "์์ธ", score: 0},
          {breed: "๊ณจ๋ ๋ฆฌํธ๋ฆฌ๋ฒ", score: 0},
          {breed: "์ํฌ์ํ๋ฆฌ์ด", score: 0},
          {breed: "์ฐ์์ฝ๊ธฐ", score: 0},
          {breed: "๋งํฐ์ฆ", score: 0},
          {breed: "ํธ๋ค", score: 0},
          {breed: "๋ถ๋", score: 0},
          {breed: "ํฌ๋ฉ๋ผ๋์", score: 0},
          {breed: "๋ณด๋์ฝ๋ฆฌ", score: 0},
          {breed: "์๋ฐ", score: 0},
          {breed: "์ง๋", score: 0},
          {breed: "์น์์", score: 0},
        ],
```


<br />

### ๐ฏMDTI ์ฑ์ ๋ฐฉ์

> `MDTI Questionnaire`์ ์ ํ์ง์์ ๊ณ ๋ฅธ Key๊ฐ๊ณผ  `ํ์ข๋ณ Question's Key`์ ๋น๊ตํ์ฌ ์ผ์นํ๋ฉด ํด๋น๋๋ ํ์ข๋ค์ `ScoreBoard`์ score๋ฅผ 1์ฉ ์ฆ๊ฐ์ํต๋๋ค. ๋ฌธ์ ์๋ฅผ ๊ฑฐ๋ญํ  ์๋ก ์ค๋ฌธ์์๊ฒ ๋ง๋ ํ์ข์ score๊ฐ ๋ง์ด ์์ด๊ฒ ๋ฉ๋๋ค. ๊ทธ๋ฆฌ๊ณ  score๋ฅผ ๊ธฐ์ค์ผ๋ก ๋ด๋ฆผ์ฐจ์์ผ๋ก ์ ๋ ฌํ์ฌ ์์ชฝ๋ถํฐ ์์ ๋ณ๋ก ์ค๋ฌธ์์๊ฒ ์ถ์ฒ๋ฉ๋๋ค.

```javascript
calculateResult({state, commit}){
          var my_answers = state.myAnswers;	//MDTI Questionnaire์ ์ ํ์ง์์ ๊ณ ๋ฅธ Key๊ฐ๋ค
          var dogs_mdti = state.dogsMdti;	//ํ์ข๋ณ Question's Key
          var mdti_score_board = state.mdtiScoreboard;	//ScoreBoard
          for(var i = 0; i < my_answers.length; i++ ){
            for(var j = 0; j < dogs_mdti.length; j++ ){
              if(!(my_answers[i] ^ dogs_mdti[j].AtQ[i])){	//XNOR์ฐ์ฐ(๊ฐ์ผ๋ฉด true, ๋ค๋ฅด๋ฉด false)
                mdti_score_board[j].score++;	//ํด๋น๋๋ ํ์ข๋ค์ score๋ฅผ 1์ฉ ์ฆ๊ฐ
              }
            }
          }
          mdti_score_board.sort(function(a, b) {  //๋ด๋ฆผ์ฐจ์์ผ๋ก ์ ๋ ฌ
            return b["score"] - a["score"];
          });
          commit('SET_MDTI_RESULT', res )
        }
```

------

<br />

## ๐ ํ์ข๋ณ ์์ํ๊ธฐ

### ๐พ ํ์ข ์ ํ

> ๋ชจ๋  ์ ๊ธฐ๊ฒฌ์ ์ ๋ณด๋ [์ขํฉ์ ๊ธฐ๊ฒฌ ๋ณดํธ์ผํฐ](https://www.zooseyo.or.kr/)์์ ํฌ๋กค๋งํ๋ฏ๋ก ์ค์  ์์์ ๊ธฐ๋ค๋ฆฌ๋ ์ ๊ธฐ๊ฒฌ๋ค์ ๋ณด์ฌ์ค๋ค
> 

<img width="20%" src="./์ฐ์ถ๋ฌผ/ํ์ข๋ณํ์ด์ง.png" />
<br />

### ๐ ์์ธํ์ด์ง

> BSP์ง์ (Breed Specific Percent) 
>
> :: Classification์ ํตํด ํด๋น ์ ๊ธฐ๊ฒฌ์ ์ธํ๊ณผ ๊ฐ์ฅ ๋ฎ์ 3์ข์ ์์น๋ก ํ์ฐํ์ฌ ๋๋์ฐจํธ๋ก ํ์

<img width="20%" src="./์ฐ์ถ๋ฌผ/์์ธํ์ด์ง.png" />
<br />

### ๐จโ๐งโ๐ฆ ์์ํ๊ธฐ

> ์์์ ํด๋น ์ ๊ธฐ๊ฒฌ์ ๊ด๋ฆฌํ๋ ์ ๊ธฐ๊ฒฌ์ผํฐ ํ์ด์ง๋ก ์ด๋ํ์ฌ ์ด๋ฃจ์ด์ง๋ค
> 
<img width="20%" src="./์ฐ์ถ๋ฌผ/์์ํ์ด์ง.png" />


------

<br />

## ๐ Contributer

#### ํ๋ก ํธ : 		์กฐํ์ญ

#### ๋ฐฑ์๋ : 		๊น์ฑ์ค, ์ง์น์ค, ์ด์๋ฏผ

#### ์ธ๊ณต์ง๋ฅ : 	์ง์์ฐ
