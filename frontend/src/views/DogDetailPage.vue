<template>
  <v-container>
    <h1 style="color: #494949">우리 아이는</h1>

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