<template>
  <v-container fill-height class="Mdti">
    <v-progress-linear
      class="step-progress ml-6"
      height="10"
      rounded
      color="deep-orange"
      :value="progress"
    ></v-progress-linear>
    <v-row justify="center" v-for="(question, idx) in questions" :key="idx">
      <v-col cols="12" class="my-16">
        <mdti-sheet :question="question" :idx="idx" />
      </v-col>
    </v-row>
    <v-row>
      <v-col align="center">
        <v-btn @click="calResult" x-large color="#f1d1d1" class="pa-8 mb-10">
          결과보기
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import MdtiSheet from "../components/MDTI/MdtiSheet.vue";
import { mapState, mapActions } from "vuex";

export default {
  components: { MdtiSheet },
  computed: {
    ...mapState(["questions", "myAnswers", "dogsMdti", "progress"]),
  },
  methods: {
    ...mapActions(["calculateResult"]),
    calResult() {
      this.$store.dispatch("calculateResult");
      this.$router.push({ name: "mdtiResult" });
    },
  },
  created() {
    this.$store.commit("SET_CURPAGE", "MdtiPage");
  },
};
</script>

<style>
.step-progress {
  position: sticky;
  top: 15px;
  width: 300px;
}
.Mdti {
  background-image: url("../assets/MDTI/MDTI배경.png");
  background-repeat: no-repeat;
  background-size: cover;
}
</style>