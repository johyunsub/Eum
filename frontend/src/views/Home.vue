<template>
  <v-container fill-height>
    <v-row>
      <v-col align="center">
        <h1>이음</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col align="center">
        <v-btn :to="'/dogs'" color="success">품종별로 매칭하기</v-btn>
        <v-btn :to="'/dbti'" color="primary">DBTI 매칭하기</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Home",
};
</script>
