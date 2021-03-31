<template>
  <v-container>
    <div class="ma-3">
      <h1 style="color: #005086">품종 선택</h1>
      <p style="color: #ff5252">*입양하실 품종을 선택해주세요</p>
    </div>
    <v-container fluid>
      <v-row dense>
        <v-col v-for="card in cards" :key="card.title" :cols="6">
          <v-card elevation="1" @click="MovePage(card.title)">
            <v-img :src="card.src" height="150px"> </v-img>
            <v-card-actions>
              <v-card-text v-text="card.title"></v-card-text>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon style="color: #ff5252">mdi-heart</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>
<script>
import Dogs from "../assets/Dogs";

export default {
  data: () => ({
    cards: [
      { title: "비숑", src: Dogs.BeeShong1, url: "" },
      { title: "시츄", src: Dogs.SeeChu1 },
      { title: "골드리트리버", src: Dogs.GoldRe1 },
      { title: "요크셔테리어", src: Dogs.YoKeShuter1 },
      { title: "웰시코기", src: Dogs.WelCi1 },
      { title: "말티즈", src: Dogs.MalTeez1 },
      { title: "푸들", src: Dogs.PuDle1 },
      { title: "불독", src: Dogs.BulDok1 },
      { title: "포메라니언", src: Dogs.PoMe1 },
      { title: "보더콜리", src: Dogs.BoDer1 },
      { title: "시바", src: Dogs.SiBa1 },
      { title: "기타", src: Dogs.etc },
    ],
  }),
  methods: {
    MovePage: function (kind) {
      this.$router.push({ name: "dogList" });
      this.$store.commit("SET_KIND", kind);
    },
  },
  created() {
    this.$store.commit("SET_CURPAGE", "DogsPage");
  },
};
</script>
<style lang="scss">
</style>
