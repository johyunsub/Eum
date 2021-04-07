<template>
  <v-container>
    <h1 style="color: #494949">우리 아이는</h1>
    <maching-chart v-if="prdLen != 0" />
    <h1>연락처: {{ dogInfo.phone }}</h1>
    <h1>url: <a v-bind:href="dogInfo.url" target="_blank">링크</a></h1>
    <h1>위치: {{ dogInfo.location }}</h1>
    <h1>성별: {{ dogInfo.sex }}</h1>
    <h1 v-if="prdLen == 0">품종: {{ dogInfo.breed }}</h1>
    <h1 v-if="prdLen != 0">품종: 믹스</h1>
  </v-container>
</template>

<script>
import MachingChart from "../components/Dogs/DogMachingChart.vue";
import { mapState } from "vuex";

export default {
  components: { MachingChart },
  computed: {
    ...mapState(["dogs", "dogListIdx", "chartInfo"]),
  },
  data: () => ({
    dogInfo: {
      breed: "",
      phone: "",
      url: "",
      files: [],
      location: "",
      sex: "",
      doginfopredicet: [],
    },
    prdLen: "",
  }),
  created() {
    this.dogInfo = this.dogs[this.dogListIdx];
    this.prdLen = this.dogInfo.doginfopredicet.length;
    // this.$store.commit("SET_CHART_INFO", this.dogInfo.doginfopredicet);
    this.$store.commit("SET_CURPAGE", "DogDetailPage");
    // console.log(this.chartInfo);
  },
};
</script>

<style>
</style>