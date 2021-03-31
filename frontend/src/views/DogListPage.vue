<template>
  <v-container>
    <h1>센터 아이들</h1>
    <p>{{ kind }}</p>
    <v-col v-for="card in cards" :key="card.no" :cols="12">
      <v-card elevation="0" @click="movePage(card.no)">
        <v-img src="../assets/Dogs/BeeShong.png" height="150px">
          {{ card.age }}살
          <font-awesome-icon
            v-if="card.gender == '수'"
            icon="mars"
            size="lg"
            style="color: #1e88e5"
          />
          <font-awesome-icon
            v-if="card.gender == '암'"
            icon="venus"
            size="lg"
            style="color: #ff5252"
          />
        </v-img>
        <v-card-title>{{ card.title }}</v-card-title>
      </v-card>
    </v-col>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "DogList",
  computed: {
    ...mapState(["kind"]),
  },
  data: () => ({
    cards: [
      {
        no: 1,
        title: "보리의 가족을 찾아요",
        age: 1,
        gender: "암",
      },
      {
        no: 2,
        title: "두리의 가족을 찾아요",
        age: 3,
        gender: "수",
      },
    ],
  }),
  methods: {
    movePage: function (no) {
      this.$router.push({ name: "dogDetail" });
      console.log(no);
    },
  },
  created() {
    this.$store.commit("SET_CURPAGE", "DogListPage");
  },
};
</script>

<style>
</style>