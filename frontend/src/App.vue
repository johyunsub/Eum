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
