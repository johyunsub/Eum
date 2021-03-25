<template>
  <div>
    <v-app-bar color="#318fb5" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>이음</v-toolbar-title>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
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

          <v-list-item :to="'/dbti'">
            <v-list-item-icon>
              <font-awesome-icon icon="feather-alt" size="lg" />
            </v-list-item-icon>
            <v-list-item-title>DBTI</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>
<script>
export default {
  name: "hearder", //이 컴포넌트의 이름 지정
  data: () => ({
    drawer: false,
    group: null,
  }),

  watch: {
    group() {
      this.drawer = false;
    },
  },
};
</script>