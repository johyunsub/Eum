<template>
  <v-container>
    <div class="ma-3">
      <h1 style="color: #494949">품종 선택</h1>
      <p style="color: #ff5252">*입양하실 품종을 선택해주세요</p>
    </div>
    <v-container fluid>
      <v-row dense>
        <v-col v-for="card in cards" :key="card.title" :cols="6">
          <v-card elevation="1" @click="MovePage(card.title)">
            <v-img :src="card.src" height="150px"> </v-img>
            <v-card-actions>
              <v-card-text v-text="card.title"></v-card-text>
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
      { title: "비숑", src: Dogs.비숑 },
      { title: "시츄", src: Dogs.시추 },
      { title: "골든리트리버", src: Dogs.골든리트리버 },
      { title: "요크셔테리어", src: Dogs.요크셔터리아 },
      { title: "웰시코기", src: Dogs.웰시코기 },
      { title: "말티즈", src: Dogs.말티즈 },
      { title: "푸들", src: Dogs.푸들 },
      { title: "불독", src: Dogs.불독 },
      { title: "포메라니안", src: Dogs.포메 },
      { title: "보더콜리", src: Dogs.보더콜리 },
      { title: "치와와", src: Dogs.치와와 },
      { title: "진도", src: Dogs.진돗개 },
      { title: "시바", src: Dogs.시바 },
      { title: "기타", src: Dogs.기타 },
    ],
  }),
  methods: {
    MovePage: function (breed) {
      this.$router.push({ name: "dogList" });
      this.$store.commit("SET_BREED", breed);
    },
  },
  created() {
    this.$store.commit("SET_CURPAGE", "DogsPage");
  },
};
</script>
<style lang="scss">
</style>
