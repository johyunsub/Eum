<template>
  <v-container fill-height class="HomePage">
    <v-row>
      <v-col align="center">
        <h1 style="color: #8d6e63">이음</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col align="center">
        <br /><br /><br /><br /><br /><br />
        <v-btn :to="'/dogs'" x-large color="#eabf9f" class="mx-1"
          >품종별 매칭하기</v-btn
        >
        <v-btn :to="'/dbti'" x-large color="#b68973" class="mx-1"
          >DBTI 매칭하기</v-btn
        >
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Home",
};
</script>
<style>
.HomePage {
  background-image: url("../assets/BgImg1.jpg");
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
