<template>
  <v-container>
    <h1 style="color: #494949">우리 아이는</h1>
       <h2 class="mt-3 ml-4">아이 정보</h2>
    <v-row class=" mb-5 mt-1">
      <v-col cols="1"></v-col>
        <v-col cols="3" >
          <v-row>
             <h3 >품종:</h3>
          </v-row>
          <v-row>
            <h3>성별:</h3>
          </v-row>
          <v-row>
            <h3>위치: </h3>
          </v-row>
          <v-row>
            <h3 v-if="dogInfo.phone != ''">연락처:</h3>
          </v-row>
        </v-col>
        <v-col cols="8" >
          <v-row justify="center">
            <h3 v-if="prdLen == 0"> {{ dogInfo.breed }}</h3>
            <h3 v-if="prdLen != 0"> 믹스</h3>
          </v-row>
          <v-row justify="center">
            <h3> {{ dogInfo.sex }}</h3>
          </v-row>
          <v-row justify="center">
            <h3>{{ dogInfo.location }}</h3>
          </v-row>
          <v-row justify="center">
            <h3>{{ dogInfo.phone }}</h3>
          </v-row>
        </v-col>
        <v-col v-for="(dogImg, i) in dogInfo.files" :key="i" :cols="12">
      <v-img :src="`data:image/jpeg;base64,${dogInfo.files[i].image}`" />
    </v-col>
    </v-row>
    <v-row v-if="prdLen != 0" class="my-4 mx-4">
      <h2>BSP지표</h2>
      <div style="color: #ff5252; font-size: 12px " style: >
        *BSP(Breed Similarity Percent)지표는 믹스견의 겉모습과 가장 유사한 세
        품종들이 표시됩니다.
      </div>
    </v-row>
    <maching-chart v-if="prdLen != 0" />

    
    <v-row>
    <v-spacer></v-spacer>
       <a v-bind:href="dogInfo.url" target="_blank" class="mr-5 my-10">
         <v-img src="../assets/icon/링크버튼.png" height="70" max-width="200" class="mx-1" /> 
       </a>
    </v-row>
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