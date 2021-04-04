import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from "./store";
import vuetify from './plugins/vuetify';

import "@/fontAwesomeIcon.js"; // fontAwesomeIcon.js 불러옴
import SequentialEntrance from "vue-sequential-entrance";
import "vue-sequential-entrance/vue-sequential-entrance.css";
Vue.use(SequentialEntrance);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App)
}).$mount('#app');
