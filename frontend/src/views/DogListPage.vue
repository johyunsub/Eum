<template>
  <v-container>
    <h1 style="color: #494949">센터 아이들</h1>
    <p style="color: #ff5252">*생김새가 {{ breed }}인 믹스견도 표시됩니다.</p>
    <v-col v-for="(card, idx) in dogs" :key="idx" :cols="12">
      <v-card elevation="0" @click="movePage(idx)">
        <v-img
          v-if="card.files.length != 0"
          :src="`data:image/jpg;base64,${card.files[0].image}`"
          height="280"
        >
        </v-img>
        <v-img
          v-if="card.files.length == 0"
          src="../assets/Dogs/사진없을시.png"
          height="330"
        >
        </v-img>
        <v-card-title class="">
          <img src="../assets/icon/house.png" height="25" class="mx-1" />
          {{ card.location }}
          <img src="../assets/icon/breed.png" height="27" class="mx-1 ml-3" />
          {{ card.breed }}
          <font-awesome-icon
            v-if="card.sex == '남아' || card.sex == '한쌍'"
            icon="mars"
            size="lg"
            class="ml-2"
            style="color: #1e88e5"
          />
          <font-awesome-icon
            v-if="card.sex == '여아' || card.sex == '한쌍'"
            icon="venus"
            size="lg"
            class="ml-2"
            style="color: #ff5252"
          />
        </v-card-title>
      </v-card>
    </v-col>
    <v-dialog v-model="loading" persistent width="300">
      <v-card color="pink accent-2" dark>
        <v-card-text class="py-2">
          잠시만 기다려주세요...
          <v-progress-linear
            indeterminate
            color="white"
            class="mb-0"
          ></v-progress-linear>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { mapActions, mapState } from "vuex";
export default {
  name: "DogList",
  computed: {
    ...mapState(["breed", "dogs", "dogId", "imgUrl"]),
  },
  data: () => ({
    loading: false,
  }),
  methods: {
    ...mapActions(["dogsData"]),

    movePage: function (idx) {
      this.$store.commit("SET_DOG_LIST_IDX", idx); //품종리스트의 몇번째인지 idx set
      this.$router.push({ name: "dogDetail" });
    },
  },
  created() {
    this.dogsData(this.breed); //해당 카드를 클릭할때 vuex에 품종에 따른 강아지데이터 저장
    this.$store.commit("SET_CURPAGE", "DogListPage"); //현재 페이지 설정
    this.$vuetify.goTo(document.body.scrollTop); //상단으로 이동
    this.loading = true;
  },
  watch: {
    loading(val) {
      if (!val) return;
      setTimeout(() => (this.loading = false), 1500);
    },
  },
};
</script>

<style>
.h1 {
  color: #494949;
}
</style>