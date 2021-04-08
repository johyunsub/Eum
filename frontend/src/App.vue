<template>
  <v-app>
    <Header v-if="homePath != 'Home'" />
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import Header from "./components/layout/Header.vue";

export default {
  components: { Header },
  name: "App",

  data: () => ({
    //
  }),
  computed: {
    homePath() {
      return this.$route.name;
    },
  },
};
</script>
<style lang="scss">
@font-face {
  font-family: "Jal_Onuel";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-10-21@1.0/Jal_Onuel.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
#app {
  font-family: "Jal_Onuel";
  background-color: #fff7ec;
}
</style>