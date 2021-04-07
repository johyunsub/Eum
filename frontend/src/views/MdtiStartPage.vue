<template>
  <v-container fill-height class="MdtiHome">
    <v-row justify="center"></v-row>
    <v-row justify="center"></v-row>

    <v-row>
      <v-col align="center">
        <v-btn :to="'/mdti'" x-large color="#ff6464" class="mb-3 pa-8" dark
          >검사 시작하기</v-btn
        >
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import mainImg from "../assets/MDTI/MDTI시작배경4.png";
export default {
  data: () => ({
    // mainImg,
  }),
  created() {
    this.$store.commit("SET_CURPAGE", "MdtiStartPage");
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