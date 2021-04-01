import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

import { createInstance } from '../api/index.js';
const instance = createInstance();

export default new Vuex.Store({
    state: {
        breed: '',   //품종에따른 강아지 페이지에서 사용되는 품종 정보 
        curPage: '',    //현재 위치하고 있는 페이지 정보 ( 페이지 이동간 사용 )
        dogs: [     //서버로부터 받아온 유기견 데이터
            {
                breed: "비숑",
                location: "대구",
                url: "test1.com",
                phone: "010-1111-1111",
                datetime: "2012-12-12 00:00:00",
                sex: "남아",
                doginfopredicet: [
                    {
                        dogid: "4444",
                        percent: "23",
                        predictedBreed: "품종1"
                    },
                    {
                        dogid: "4444",
                        percent: "23",
                        predictedBreed: "품종1"
                    },
                    {
                        dogid: "4444",
                        percent: "23",
                        predictedBreed: "품종1"
                    }
                ],
                doginfoimages: [
                    {
                        id: "6",
                        dogid: "4444",
                        fileId: "4"
                    }
                ],
                files: [
                    {
                        id: "4",
                        path: "C:\\Users\\sskim\\Downloads\\Dogs\\골든리트리버",
                        originName: "리트리버",
                        systemName: "골든리트리버_337379_04dffff6-87a4-11eb-a586-08d23e250ad9.jpg",
                        size: "0",
                        type: "jpg",
                        imageBytes: ""
                    },]
            },
            {
                breed: "비숑",
                location: "구미",
                url: "test2.com",
                phone: "010-2222-2222",
                datetime: "2020-11-11 00:00:00",
                sex: "남아",
                doginfopredicet: [
                    {
                        dogid: "4444",
                        percent: "23",
                        predictedBreed: "품종1"
                    },
                    {
                        dogid: "4444",
                        percent: "23",
                        predictedBreed: "품종1"
                    },
                    {
                        dogid: "4444",
                        percent: "23",
                        predictedBreed: "품종1"
                    }
                ],
                doginfoimages: [
                    {
                        id: "6",
                        dogid: "4444",
                        fileId: "4"
                    }
                ],
                files: [
                    {
                        id: "4",
                        path: "C:\\Users\\sskim\\Downloads\\Dogs\\골든리트리버",
                        originName: "리트리버",
                        systemName: "골든리트리버_337379_04dffff6-87a4-11eb-a586-08d23e250ad9.jpg",
                        size: "0",
                        type: "jpg",
                        imageBytes: ""
                    },]
            },
            {
                breed: "믹스",
                location: "부산",
                url: "test3.com",
                phone: "010-3333-3333",
                datetime: "2021-03-31 00:00:00",
                sex: "여아",
                doginfopredicet: [
                    {
                        dogid: "4444",
                        percent: "23",
                        predictedBreed: "비숑"
                    },
                    {
                        dogid: "4444",
                        percent: "23",
                        predictedBreed: "푸들"
                    },
                    {
                        dogid: "4444",
                        percent: "23",
                        predictedBreed: "품종1"
                    }
                ],
                doginfoimages: [
                    {
                        id: "6",
                        dogid: "4444",
                        fileId: "4"
                    }
                ],
                files: [
                    {
                        id: "4",
                        path: "C:\\Users\\sskim\\Downloads\\Dogs\\골든리트리버",
                        originName: "리트리버",
                        systemName: "골든리트리버_337379_04dffff6-87a4-11eb-a586-08d23e250ad9.jpg",
                        size: "0",
                        type: "jpg",
                        imageBytes: ""
                    },]
            },
        ],   
    },
    mutations: {
        SET_BREED(state, data){
            state.breed = data;
        },
        SET_CURPAGE(state, data){
            state.curPage = data;
        },
        SET_DOGS(state, data){
            state.dogs = data;
        }
    },
    actions: {
        dogsData({state, commit}, breed) {
            instance
            .get(`/iuem/doginfo/breed/${breed}/0/1`)
            .then((res) => {
                commit('SET_DOGS', res.data );
                console.log(state.dogs);
            })
            .catch((err) => console.log(err.response));
        }
    },
    modules: {}
})