import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        kind: '',   //품종에따른 강아지 페이지에서 사용되는 품종 정보 
        curPage: '',
    },
    mutations: {
        SET_KIND(state, data){
            state.kind = data;
        },
        SET_CURPAGE(state, data){
            state.curPage = data;
        }
    },
    actions: {},
    modules: {}
})