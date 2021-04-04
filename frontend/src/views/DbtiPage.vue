<template>
  <div class="container-app">
    <div class="container-quiz">
      <div class="header-quiz">
        <h1>Dog MBTI</h1>
      </div>
      <div class="step-progress" :style="{ width: progress + '%' }"></div>
      <div
        class="box"
        v-for="(question, index) in questions.slice(a, b)"
        :key="index"
        v-show="quiz"
      >
        <div class="box-question">
          <h2>Question {{ b }}/{{ questions.length }}</h2>
          <p></p>
          <h3>{{ question.question }}</h3>
        </div>
        <div class="box-propositions">
          <ul>
            <li
              v-for="(proposition, index) in question.propositions"
              :key="index"
              class="li"
              @click="selectResponse(proposition, index)"
              :class="true ? check(proposition) : ''"
            >
              {{ proposition.props }}
              <div
                class="fas fa-check"
                v-if="correct ? proposition.correct : ''"
              ></div>
              <div
                class="fas fa-times"
                v-if="correct ? !proposition.correct : ''"
              ></div>
            </li>
          </ul>
        </div>
      </div>
      <div class="box-score" v-if="score_show">
        <h2>당신과 가장 잘맞는 강아지는</h2>
        <h2>{{ this.result }}</h2>
        <div class="btn-restart">
          <button @click="restartQuiz">
            Restart <i class="fas fa-sync-alt"></i>
          </button>
        </div>
      </div>
      <div class="footer-quiz">
        <div v-if="progress < 100" class="box-button">
          <button
            @click="skipQuestion()"
            :style="
              question_status[a].prev
                ? 'background-color: rgb(106, 128, 202)'
                : ''
            "
          >
            Prev
          </button>
          <button
            @click="nextQuestion()"
            :style="
              question_status[a].next
                ? 'background-color: rgb(106, 128, 202)'
                : ''
            "
          >
            Next
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'

export default {
  data() {
    return {
      questions: [
        {
          question: "개의 털이 빠진다면...??",
          propositions: [
            { props: "상관없다", correct: false, compare: 0 },
            { props: "어느 정도 괜찮다", correct: false, compare: 0.4 },
            { props: "예민하다", correct: false, compare: 0.7 },
          ],
          weight: 0.3,
        },
        {
          question: "함께 살기에 적당한 개의 크기는...??",
          propositions: [
            { props: "5kg 이하 소형견", correct: false },
            { props: "10kg 안팎의 중형견", correct: false },
            { props: "15kg 이상 대형견", correct: false },
          ],
          weight: 0.2,
        },
        {
          question: "하루에 산책 가능한 시간은...??",
          propositions: [
            { props: "집 주변에서 가벼운 산책", correct: false, compare: 0 },
            { props: "2시간 이상 산책", correct: false, compare: 1 },
          ],
          weight: 0.15,
        },
        {
          question: "우리집 개가 짖는 정도는...??",
          propositions: [
            {
              props: "많이 짖지 않았으면 좋겠다",
              correct: false,
              compare: 0.5,
            },
            {
              props: "많이 짖어도 훈련으로 극복할 수 있다.",
              correct: false,
              compare: 0,
            },
          ],
          weight: 0.2,
        },
        {
          question: "가족이 집을 비우는 경우는...??",
          propositions: [
            {
              props: "가족이 집에 있는 경우가 많다.",
              correct: false,
              compare: 0,
            },
            { props: "때때로 모두 집을 비운다.", correct: false, compare: 0.5 },
          ],
          weight: 0.1,
        },
        {
          question: "키우고 싶은 개의 이미지는...??",
          propositions: [
            {
              props: "인기 많은 품종 중 하나였으면...",
              correct: false,
              compare: 1,
            },
            {
              props: "내가 좋다면 아무래도 상관없다.",
              correct: false,
              compare: 0,
            },
          ],
          weight: 0.05,
        },
      ],
      question_status: [
        { prev: false, next: false },
        { prev: true, next: false },
        { prev: true, next: false },
        { prev: true, next: false },
        { prev: true, next: false },
        { prev: true, next: false },
      ],
      image:
        "https://images.mypetlife.co.kr/content/uploads/2019/09/04222847/dog-panting-1024x683.jpg",
      dog_list: [
        {
          name: "비숑",
          img: "",
          percent: 0,
          desc: "",
          weight: [1, [1, 0, 0], 0, 0.5, 0.8, 1],
        },
        {
          name: "시츄",
          img: "",
          percent: 0.0,
          desc: "",
          weight: [0.9, [1, 0, 0], 0, 0.7, 0.8, 1],
        },
        {
          name: "골드리트리버",
          img: "",
          percent: 0.0,
          desc: "",
          weight: [0.1, [0, 0, 1], 1, 0.7, 0.3, 1],
        },
        {
          name: "요크셔테리어",
          img: "",
          percent: 0.0,
          desc: "",
          weight: [0.7, [1, 0, 0], 0, 0.4, 0.3, 1],
        },
        {
          name: "웰시코기",
          img: "",
          percent: 0.0,
          desc: "",
          weight: [0.2, [0, 1, 0], 1, 0.2, 0.5, 0],
        },
        {
          name: "말티즈",
          img: "",
          percent: 0.0,
          desc: "",
          weight: [0.7, [1, 0, 0], 0, 0.2, 0.5, 1],
        },
        {
          name: "푸들",
          img: "",
          percent: 0.0,
          desc: "",
          weight: [0.8, [1, 0, 0], 0, 0.7, 0.2, 1],
        },
        {
          name: "불독",
          img: "",
          percent: 0.0,
          desc: "",
          weight: [0.4, [0, 1, 0], 0, 0.8, 0.5, 0],
        },
        {
          name: "포메라니안",
          img: "",
          percent: 0.0,
          desc: "",
          weight: [0.1, [1, 0, 0], 0, 0.4, 0.6, 1],
        },
        {
          name: "보더콜리",
          img: "",
          percent: 0.0,
          desc: "",
          weight: [0.1, [0, 0, 1], 1, 0.5, 0.1, 0],
        },
        {
          name: "시바",
          img: "",
          percent: 0.0,
          desc: "",
          weight: [0.2, [0, 1, 0], 1, 0.5, 0.7, 0],
        },
        {
          name: "진도",
          img: "",
          percent: 0.0,
          desc: "",
          weight: [0.1, [0, 0, 1], 1, 0.5, 0.5, 0],
        },
        {
          name: "치와와",
          img: "",
          percent: 0.0,
          desc: "",
          weight: [0.4, [1, 0, 0], 0, 0.3, 0.7, 1],
        },
      ],
      a: 0,
      b: 1,
      next: true,
      score_show: false,
      quiz: true,
      score: 0,
      correct: false,
      progress: 0,
      result: "",
    };
  },
  name: "DBTI",
  components: {
    //HelloWorld
  },
  computed: {},
  methods: {
    selectResponse(e) {
      for (let i = 0; i < this.questions[this.a].propositions.length; i++) {
        this.questions[this.a].propositions[i].correct = false;
      }
      e.correct = true;
      this.correct = true;
      this.question_status[this.a].next = true;
      if (e.correct) {
        this.score++;
      }
    },
    check(status) {
      if (status.correct) {
        return "correct";
      } else {
        return "incorrect(x)";
      }
    },
    nextQuestion() {
      if (!this.question_status[this.a].next) {
        return;
      }
      this.progress = this.progress + 100 / this.questions.length;
      if (this.questions.length - 1 == this.a) {
        //계산하는 함수로 묶고 호출해주기
        //여기서부터

        for (let q = 0; q < this.questions.length; q++) {
          if (q == 1) {
            for (let i = 0; i < 3; i++) {
              if (this.questions[q].propositions[i].correct == true) {
                for (let j = 0; j < this.doglist.length; j++) {
                  this.dog_list[j].percent +=
                    this.dog_list[j].weight[q][i] * this.questions[q].weight;
                }
              }
            }

            continue;
          }

          for (let i = 0; i < this.questions[q].propositions.length; i++) {
            if (this.questions[q].propositions[i].correct == true) {
              for (let j = 0; j < this.dog_list.length; j++) {
                if (
                  this.questions[q].propositions[i].compare <=
                  this.dog_list[j].weight[q]
                ) {
                  this.dog_list[j].percent +=
                    this.dog_list[j].weight[q] * this.questions[q].weight;
                }
              }
            }
          }
        }

        this.dog_list.sort(function (a, b) {
          return b["percent"] - a["percent"];
        });
        console.log(this.dog_list[0]); //제일 잘맞는 강아지!
        console.log(this.dog_list[1]); //두번째!
        console.log(this.dog_list[2]);
        console.log(this.dog_list[3]);
        ////여기까지
        this.score_show = true;
        this.quiz = false;
      } else {
        this.a++;
        this.b++;
        this.correct = false;
        this.next = true;
      }
    },
    skipQuestion() {
      if (!this.question_status[this.a].prev) {
        return;
      }
      this.progress = this.progress - 100 / this.questions.length;

      if (0 == this.a) {
        this.score_show = true;
        this.quiz = false;
      } else {
        this.a--;
        this.b--;
      }
    },

    restartQuiz() {
      Object.assign(this.$data, this.$options.data()); // reset data in vue
    },
  },
  created() {
    this.$store.commit("SET_CURPAGE", "DBTI");
  },
};
</script>
