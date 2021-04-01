<template>
  <v-container>
    <h1>센터 아이들</h1>
    <p>{{ breed }}</p>
    <v-col v-for="card in dogs" :key="card.no" :cols="12">
      <v-card elevation="0" @click="movePage(card.no)">
        <v-img src="../assets/Dogs/비숑.png" height="150px">
          {{}}살
          <font-awesome-icon
            v-if="card.sex == '남아'"
            icon="mars"
            size="lg"
            style="color: #1e88e5"
          />
          <font-awesome-icon
            v-if="card.sex == '여아'"
            icon="venus"
            size="lg"
            style="color: #ff5252"
          />
        </v-img>
        <v-card-title>{{ card.phone }}</v-card-title>
      </v-card>
    </v-col>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "DogList",
  computed: {
    ...mapState(["breed", "dogs"]),
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