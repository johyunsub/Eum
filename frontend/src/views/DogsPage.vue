<template>
  <v-container>
    <div class="ma-3">
      <h1 style="color: #005086">품종 선택</h1>
      <subtitle-1 style="color: #ff5252"
        >*입양하실 품종을 선택해주세요</subtitle-1
      >
    </div>
    <v-container fluid>
      <v-row dense>
        <v-col cols="6">
          <v-card elevation="1">
            <v-img src="../assets/Dogs/BeeShong1.png" height="150px"> </v-img>
            <v-card-actions>
              <v-card-text>비숑</v-card-text>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon style="color: #ff5252">mdi-heart</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card elevation="1">
            <v-img src="@/assets/Dogs/SeeChu1.jpg" height="150px"> </v-img>
            <v-card-actions>
              <v-card-text>시츄</v-card-text>
              <v-spacer></v-spacer>
              <v-btn icon
                ><v-icon style="color: #ff5252">mdi-heart</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card elevation="1">
            <v-img src="@/assets/Dogs/GoldRe1.png" height="150px"> </v-img>
            <v-card-actions>
              <v-card-text>골드리트리버</v-card-text>
              <v-spacer></v-spacer>
              <v-btn icon
                ><v-icon style="color: #ff5252">mdi-heart</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card elevation="1">
            <v-img src="@/assets/Dogs/YoKeShuter1.png" height="150px"> </v-img>
            <v-card-actions>
              <v-card-text>요크셔테리어</v-card-text>
              <v-spacer></v-spacer>
              <v-btn icon
                ><v-icon style="color: #ff5252">mdi-heart</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card elevation="1">
            <v-img src="../assets/Dogs/WelCi1.png" height="150px"> </v-img>
            <v-card-actions>
              <v-card-text>웰시코기</v-card-text>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon style="color: #ff5252">mdi-heart</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card elevation="1">
            <v-img src="@/assets/Dogs/MalTeez1.png" height="150px"> </v-img>
            <v-card-actions>
              <v-card-text>말티즈</v-card-text>
              <v-spacer></v-spacer>
              <v-btn icon
                ><v-icon style="color: #ff5252">mdi-heart</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card elevation="1">
            <v-img src="@/assets/Dogs/PuDle1.png" height="150px"> </v-img>
            <v-card-actions>
              <v-card-text>푸들</v-card-text>
              <v-spacer></v-spacer>
              <v-btn icon
                ><v-icon style="color: #ff5252">mdi-heart</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card elevation="1">
            <v-img src="@/assets/Dogs/BulDok1.png" height="150px"> </v-img>
            <v-card-actions>
              <v-card-text>불독</v-card-text>
              <v-spacer></v-spacer>
              <v-btn icon
                ><v-icon style="color: #ff5252">mdi-heart</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card elevation="1">
            <v-img src="@/assets/Dogs/PoMe1.png" height="150px"> </v-img>
            <v-card-actions>
              <v-card-text>포메라니안</v-card-text>
              <v-spacer></v-spacer>
              <v-btn icon
                ><v-icon style="color: #ff5252">mdi-heart</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card elevation="1">
            <v-img src="@/assets/Dogs/BoDer1.png" height="150px"> </v-img>
            <v-card-actions>
              <v-card-text>보더콜리</v-card-text>
              <v-spacer></v-spacer>
              <v-btn icon
                ><v-icon style="color: #ff5252">mdi-heart</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card elevation="1">
            <v-img src="@/assets/Dogs/SiBa1.png" height="150px"> </v-img>
            <v-card-actions>
              <v-card-text>시바</v-card-text>
              <v-spacer></v-spacer>
              <v-btn icon
                ><v-icon style="color: #ff5252">mdi-heart</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="6">
          <v-card elevation="1">
            <v-img src="@/assets/Dogs/etc.jpg" height="150px"> </v-img>
            <v-card-actions>
              <v-card-text>기타</v-card-text>
              <v-spacer></v-spacer>
              <v-btn icon
                ><v-icon style="color: #ff5252">mdi-heart</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>
<script>
export default {
  data: () => ({
    cards: [
      {
        title: "비숑2",
        flex: 6,
      },
      {
        title: "포메라니안",
        src: "@/assets/Dogs/PoMe.png",
        flex: 6,
      },
    ],
  }),
};
</script>
<style lang="scss">
</style>
