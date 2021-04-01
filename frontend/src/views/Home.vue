<template>
  <v-container fill-height class="HomePage">
    <v-row>
      <v-col align="center">
        <br /><br /><br />
        <v-btn :to="'/dogs'" x-large color="#f1d1d1" class="mx-2"
          >품종별<br />
          입양하기</v-btn
        >
        <v-btn :to="'/dbti'" x-large color="#f2c6b4" class="mx-2"
          >DBTI<br />
          작성하기</v-btn
        >
      </v-col>
    </v-row>
    <v-row>
      <v-col align="center"> </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Home",
  created() {
    this.$store.commit("SET_CURPAGE", "Home");
  },
};
</script>
<style>
.HomePage {
  background-image: url("../assets/이음홈.png");
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
