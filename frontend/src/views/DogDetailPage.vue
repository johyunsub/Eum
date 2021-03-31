<template>
  <v-container>
    <h1>유기견상세페이지</h1>
    <maching-chart />
  </v-container>
</template>

<script>
import MachingChart from "../components/Dogs/DogMachingChart.vue";

export default {
  components: { MachingChart },
  created() {
    this.$store.commit("SET_CURPAGE", "DogDetailPage");
  },
};
</script>

<style>
</style>