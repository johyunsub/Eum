<template>
  <div id="app">
    <Header />
    <h1>{{ currentPath }}</h1>
    <div id="content" class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Header from "./components/layout/Header.vue";

export default {
  name: "App",
  components: {
    Header,
  },
  computed: {
    currentPath() {
      return this.$router.path;
    },
  },
};
</script>

<style>
</style>
