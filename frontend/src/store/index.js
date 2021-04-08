import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

import { createInstance } from '../api/index.js';
const instance = createInstance();

export default new Vuex.Store({
    state: {
        dialogOn: true,
        breed: '',   //품종에따른 강아지 페이지에서 사용되는 품종 정보 
        dogs: [],    //서버로부터 받아온 유기견 데이터
        curPage: '',    //현재 위치하고 있는 페이지 정보 ( 페이지 이동간 사용 )
        dogListIdx: 0, //품종매칭 리스트에서 몇번째 개정보를 상세페이지로 넘겨줄건지 Index
        chartInfo: [],
        progress: 0,
        myAnswers: [false, false, false, false, false, false],   //MDTI에서 작성한 나의 답안
        myAnswersAccuracy: [0, 0, 0, 0, 0, 0],  //MDTI에서 작성한 나의 답안과 모범답안의 차이의 수치
        dogsMdti: [     //MDTI에서 활용되는 품종에따른 질문에따른 답(Answer the Question)
            {breed: "비숑", AtQ: [false, false, true, false, false, true] },
            {breed: "시츄", AtQ: [true, false, true, false, true, false] },
            {breed: "골든리트리버", AtQ: [true, true, false, true, true, true] },
            {breed: "요크셔테리어", AtQ: [false, true, true, false, true, false] },
            {breed: "웰시코기", AtQ: [false, false, true, false, true, true] },
            {breed: "말티즈", AtQ: [true, false, true, true, false, false] },
            {breed: "푸들", AtQ: [false, false, true, true, false, true] },
            {breed: "불독", AtQ: [false, true, true, false, true, true] },
            {breed: "포메라니안", AtQ: [true, false, true, true, false, true] },
            {breed: "보더콜리", AtQ: [true, true, false, false, true, false] },
            {breed: "시바", AtQ: [false, false, false, false, true, true] },
            {breed: "진도", AtQ: [false, false, false, true, true, false] },
            {breed: "치와와", AtQ: [false, false, true, true, false, false] },
        ],
        mdtiScoreboard: [   //MDTI에서 작성된 설문을 바탕으로 유저와 가장 맞는 강아지를 추천해주기위한 점수판
          {breed: "비숑", score: 0},
          {breed: "시츄", score: 0},
          {breed: "골든리트리버", score: 0},
          {breed: "요크셔테리어", score: 0},
          {breed: "웰시코기", score: 0},
          {breed: "말티즈", score: 0},
          {breed: "푸들", score: 0},
          {breed: "불독", score: 0},
          {breed: "포메라니안", score: 0},
          {breed: "보더콜리", score: 0},
          {breed: "시바", score: 0},
          {breed: "진도", score: 0},
          {breed: "치와와", score: 0},
        ],
        mdtiResult: {breed: "", accuracy: 0}, //나에게 맞는 강아지 MDTI결과
        
        questions: [
            {
              question: "반려견의 털이 빠진다면...",
              propositions: [
                { no: 11, props: "상관없다", correct: true, accuracy: 0.93 },
                { no: 12, props: "어느 정도 괜찮다", correct: true, accuracy: 0.81 },
                { no: 13, props: "예민하다", correct: false, accuracy: 0.93 },
              ],
              solved: false,
            },
            {
              question: "함께 살기에 적당한 반려견의 크기는...",
              propositions: [
                { no: 21, props: "5kg 이하 소형견", correct: false, accuracy: 0.93},
                { no: 22, props: "10kg 안팎의 중형견", correct: false, accuracy: 0.71},
                { no: 23, props: "15kg 이상 대형견", correct: true, accuracy: 0.93},
              ],
              solved: false,
            },
            {
              question: "하루에 산책 가능한 시간은...",
              propositions: [
                { no: 31, props: "집 주변에서 가벼운 산책", correct: true, accuracy: 0.93 },
                { no: 32, props: "2시간 이상 산책", correct: false, accuracy: 0.93 },
              ],
              solved: false,
            },
            {
              question: "우리집 반려견이 짖는 정도는...",
              propositions: [
                { no: 41, props: "많이 짖지 않았으면 좋겠다", correct: false, accuracy: 0.93,},
                { no: 42, props: "짖음 훈련으로 극복 가능하다", correct: true, accuracy: 0.93, },
              ],
              solved: false,
            },
            {
              question: "가족이 집을 비우는 경우는...",
              propositions: [
                { no: 51, props: "가족이 집에 있는 경우가 많다.", correct: false, accuracy: 0.93, },
                { no: 52, props: "때때로 모두 집을 비운다.", correct: true, accuracy: 0.55 },
              ],
              solved: false,
            },
            {
              question: "키우고 싶은 반려견의 이미지는...",
              propositions: [
                { no: 61, props: "인기 많은 품종 중 하나였으면", correct: true, accuracy: 0.93, },
                { no: 62, props: "내가 좋다면 아무래도 상관없다.", correct: false, accuracy: 0.93, },
              ],
              solved: false,
            },
          ],
        isError: '',
    },
    mutations: {
        SET_BREED(state, data){
          state.breed = data;
        },
        SET_CURPAGE(state, data){
          state.curPage = data;
        },
        SET_CHART_INFO(state, data){
          for(var i=0, j=0; i<data.length; i++){
              state.chartInfo[j++] =  data[i].doginfopredicet[0];
              state.chartInfo[j++] =  data[i].doginfopredicet[1];
              state.chartInfo[j++] =  data[i].doginfopredicet[2];
          }
        },
        SET_DOG_LIST_IDX(state, data){
          state.dogListIdx = data;
        },
        SET_DOGS(state, data){
          state.dogs = data;
        },
        SET_PROGRESS(state, data){
          state.progress += 100/data;
        },
        SET_MYANSWER(state, data){
          state.myAnswers[data.qn] = data.ans;
          state.myAnswersAccuracy[data.qn] = data.acc;
        },
        INIT_SCORE_BOARD(state) {
          state.mdtiScoreboard = [  
            {breed: "비숑", score: 0},
            {breed: "시츄", score: 0},
            {breed: "골든리트리버", score: 0},
            {breed: "요크셔테리어", score: 0},
            {breed: "웰시코기", score: 0},
            {breed: "말티즈", score: 0},
            {breed: "푸들", score: 0},
            {breed: "불독", score: 0},
            {breed: "포메라니안", score: 0},
            {breed: "보더콜리", score: 0},
            {breed: "시바", score: 0},
            {breed: "진도", score: 0},
            {breed: "치와와", score: 0},
          ];
        },
        SET_MDTI_RESULT(state, data){
          state.mdtiResult.breed = data.breed;
          state.mdtiResult.accuracy = data.accuracy;
        },
    },
    actions: {
        dogsData({ commit}, breed) {
            instance
            .get(`/iuem/doginfo/breed/${breed}/0/7`)
            .then((res) => {
                commit('SET_DOGS', res.data.data );
                commit('SET_CHART_INFO', res.data.data )
            })
            .catch((err) => {
              console.log( err.response);
              commit('SET_ERROR', true);
            });
        },
        calculateResult({state, commit}){
          var my_answers = state.myAnswers;
          var dogs_mdti = state.dogsMdti;
          var mdti_score_board = state.mdtiScoreboard;
          var my_answers_accuracy = state.myAnswersAccuracy;
          for(var i = 0; i < my_answers.length; i++ ){
            for(var j = 0; j < dogs_mdti.length; j++ ){
              if(!(my_answers[i] ^ dogs_mdti[j].AtQ[i])){
                mdti_score_board[j].score++;
              }
            }
          }
          mdti_score_board.sort(function(a, b) {
            return b["score"] - a["score"];
          });
          var acc = my_answers_accuracy.reduce((a, b) => a + b, 0)/my_answers_accuracy.length;  
          acc = parseInt(acc*1000)/10
          var res = { breed: mdti_score_board[0].breed, accuracy: acc}
          commit('SET_MDTI_RESULT', res )
        }
    },
    modules: {}
})