<template>
  <v-container fill-height class="HomePage">
    <v-row>
      <v-col align="center" class="buttons">
        <v-btn :to="'/dogs'" x-large color="#f1d1d1" class="mx-2"
          >품종별<br />
          입양하기</v-btn
        >
        <v-btn :to="'/mdtiStart'" x-large color="#f2c6b4" class="mx-2"
          >MDTI<br />
          작성하기</v-btn
        >
      </v-col>
    </v-row>
    <v-dialog
      v-model="dialog"
      transition="dialog-top-transition"
      max-width="600"
    >
      <template v-slot:default="dialog">
        <v-card class="dialog">
          <v-toolbar color="primary" dark>
            <v-icon class="mx-2">mdi-alert-circle-outline</v-icon>잠깐
            <v-spacer></v-spacer>
            <v-btn text @click="dialog.value = false">
              <v-icon>mdi-close-thick</v-icon>
            </v-btn>
          </v-toolbar>
          <v-img src="../assets/모바일팝업.png"></v-img>
        </v-card>
      </template>
    </v-dialog>
  </v-container>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "Home",
  computed: {
    ...mapState(["dialogOn"]),
  },
  created() {
    this.$store.commit("SET_CURPAGE", "Home");
    this.dialog = this.dialogOn;
    this.$store.state.dialogOn = false;
  },
  data: () => ({
    dialog: false,
  }),
};
</script>
<style>
.HomePage {
  background-image: url("../assets/이음홈.png");
  background-repeat: no-repeat;
  background-size: cover;
}
.buttons {
  position: absolute;
  top: 220px;
}
</style>
