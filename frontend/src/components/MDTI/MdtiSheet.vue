<template>
  <v-sheet class="pa-3 ma-5 my-5" shaped elevation="2" color="#fbf4f9">
    <h1 class="mt-3" style="color: #ff4d4d">Q{{ idx + 1 }}.</h1>
    <h2 class="mb-3" style="color: #ff8364">{{ question.question }}</h2>
    <v-img :src="QuestionImgSrc(idx)"> </v-img>
    <v-list ref="list" class="my-5" color="#fbf4f9">
      <v-list-item-group active-class="pink--text">
        <template v-for="(item, index) in question.propositions">
          <v-list-item :key="item.id" @click="CheckAnswer(item.no)">
            <template v-slot:default="{ active }">
              <v-list-item-content>
                <v-list-item-title
                  class="text--primary"
                  v-text="item.props"
                ></v-list-item-title>
              </v-list-item-content>

              <v-list-item-action>
                <v-icon v-if="active" color="yellow darken-3"
                  >mdi-checkbox-marked-circle</v-icon
                >
              </v-list-item-action>
            </template>
          </v-list-item>

          <v-divider
            v-if="index < question.propositions.length - 1"
            :key="index"
          ></v-divider>
        </template>
      </v-list-item-group>
    </v-list>
  </v-sheet>
</template>

<script>
import QuestionImg from "../../assets/MDTI";
import { mapState } from "vuex";

export default {
  props: {
    question: Object,
    idx: Number,
  },
  computed: {
    ...mapState(["questions", "dogsMdti"]),
    target() {
      return this.$refs.list;
    },
    options() {
      return {
        duration: 600,
        offset: -200,
        easing: "easeInOutCubic",
      };
    },
  },
  data: () => ({
    valid: false,
  }),
  methods: {
    aa() {
      this.$vuetify.goTo(document.body.scrollTop);
    },
    CheckAnswer(no) {
      this.$vuetify.goTo(this.target, this.options);

      this.$store.commit("SET_PROGRESS", this.questions.length);
      const questionNo = parseInt(no / 10) - 1;
      const PropsNo = (no % 10) - 1;
      var answer = this.questions[questionNo].propositions[PropsNo].correct;
      const accuracy = this.questions[questionNo].propositions[PropsNo]
        .accuracy;
      this.$store.commit("SET_MYANSWER", {
        qn: questionNo,
        ans: answer,
        acc: accuracy,
      });
    },
    isValid() {
      console.log("안녕");
    },
    QuestionImgSrc(idx) {
      switch (idx) {
        case 0:
          return QuestionImg.Q1;
        case 1:
          return QuestionImg.Q2;
        case 2:
          return QuestionImg.Q3;
        case 3:
          return QuestionImg.Q4;
        case 4:
          return QuestionImg.Q5;
        case 5:
          return QuestionImg.Q6;
      }
    },
  },
};
</script>

<style>
</style>