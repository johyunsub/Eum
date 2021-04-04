<template>
  <v-container>
    <h1>MDTI</h1>
    <div class="step-progress" :style="{ width: progress + '%' }"></div>
    <v-row justify="center" v-for="(question, idx) in questions" :key="idx">
      <v-col cols="12" class="mb-16">
        <mdti-sheet :question="question" :idx="idx" />
      </v-col>
    </v-row>
    <v-row>
      <v-col align="center">
        <v-btn @click="calResult" x-large color="#f1d1d1" class="mb-3">
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
    this.$store.commit("SET_CURPAGE", "MDTI");
  },
};
</script>

<style>
.step-progress {
  position: sticky;
  top: 10px;
}
</style>