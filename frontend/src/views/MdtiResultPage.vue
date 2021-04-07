<template>
  <v-container fill-height class="MdtiResult">
    <v-row class="resultImg pa-3">
      <v-col align="center" cols="12">
        <h1>{{ mdtiResult.breed }}</h1>
      </v-col>
      <v-img :src="resultImg()" height="300" max-width="350"> </v-img>
      <v-col align="center" cols="12">
        <h1>추천지수: {{ mdtiResult.accuracy }}%</h1>
      </v-col>
      <v-btn :to="'/mdtiStart'">다시하기</v-btn>
    </v-row>
    <v-row> </v-row>
  </v-container>
</template>

<script>
import resultImage from "../assets/MDTI";
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState(["mdtiResult"]),
  },
  methods: {
    resultImg() {
      switch (this.mdtiResult.breed) {
        case "비숑":
          return resultImage.비숑;
        case "시츄":
          return resultImage.시츄;
        case "골든리트리버":
          return resultImage.골든리트리버;
        case "요크셔테리어":
          return resultImage.요크셔테리어;
        case "웰시코기":
          return resultImage.웰시코기;
        case "말티즈":
          return resultImage.말티즈;
        case "푸들":
          return resultImage.푸들;
        case "불독":
          return resultImage.불독;
        case "포메라니안":
          return resultImage.포메라니안;
        case "보더콜리":
          return resultImage.보더콜리;
        case "시바":
          return resultImage.시바;
        case "진도":
          return resultImage.진도;
        case "치와와":
          return resultImage.치와와;
      }
    },
  },
};
</script>

<style>
.MdtiResult {
  background-image: url("../assets/MDTI/MDTI결과배경.png");
  background-repeat: no-repeat;
  background-size: cover;
}
.resultImg {
  position: absolute;
  top: 170px;
}
</style>