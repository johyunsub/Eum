<template>
  <div>
    <v-app-bar color="#ff8c94" dark>
      <v-app-bar-nav-icon @click="movePage">
        <font-awesome-icon icon="chevron-left" size="lg" />
      </v-app-bar-nav-icon>
      <v-toolbar-title @click="goHome">
        <img src="../../assets/logo.png" height="50" class="mt-3"
      /></v-toolbar-title>
      <v-spacer />
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="pink--text text--accent-4"
        >
          <v-list-item :to="'/'">
            <v-list-item-icon>
              <font-awesome-icon icon="home" size="lg" />
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>

          <v-list-item :to="'/dogs'">
            <v-list-item-icon>
              <font-awesome-icon icon="paw" size="lg" />
            </v-list-item-icon>
            <v-list-item-title>품종매칭</v-list-item-title>
          </v-list-item>

          <v-list-item :to="'/mdtiStart'">
            <v-list-item-icon>
              <font-awesome-icon icon="feather-alt" size="lg" />
            </v-list-item-icon>
            <v-list-item-title>MDTI</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>
<script>
import { mapState } from "vuex";

export default {
  name: "hearder", //이 컴포넌트의 이름 지정
  computed: {
    ...mapState(["curPage"]),
  },
  data: () => ({
    drawer: false,
    group: null,
  }),

  watch: {
    group() {
      this.drawer = false;
    },
  },
  methods: {
    goHome() {
      this.$router.push({ name: "Home" });
    },
    movePage() {
      switch (this.curPage) {
        case "DogsPage":
          this.$router.push({ name: "Home" });
          break;
        case "DogListPage":
          this.$router.push({ name: "dogs" });
          break;
        case "DogDetailPage":
          this.$router.push({ name: "dogList" });
          break;
        case "MdtiStartPage":
          this.$router.push({ name: "Home" });
          break;
        case "MdtiPage":
          this.$router.push({ name: "mdtiStart" });
          break;
        case "MdtiResultPage":
          this.$router.push({ name: "mdti" });
          break;
      }
    },
  },
};
</script>