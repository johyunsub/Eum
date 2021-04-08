<template>
  <v-container fill-height class="MdtiHome">
    <v-row justify="center"></v-row>
    <v-row justify="center"></v-row>

    <v-row>
      <v-col align="center">
        <v-btn :to="'/mdti'" x-large color="#ff6464" class="mb-3 pa-8" dark
          >검사 시작하기
          <font-awesome-icon class="ml-2" icon="feather-alt" size="lg" />
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({}),
  created() {
    this.$store.commit("SET_CURPAGE", "MdtiStartPage");
    this.$store.state.myAnswers = [false, false, false, false, false, false];
    this.$store.state.myAnswersAccuracy = [0, 0, 0, 0, 0, 0];
    this.$store.state.progress = 0;
    this.$store.commit("INIT_SCORE_BOARD");
  },
};
</script>

<style>
.MdtiHome {
  background-image: url("../assets/MDTI/MDTI시작배경.png");
  background-repeat: no-repeat;
  background-size: cover;
}
</style>