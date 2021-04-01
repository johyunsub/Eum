import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from "./store";
import vuetify from './plugins/vuetify';

import "@/fontAwesomeIcon.js"; // fontAwesomeIcon.js 불러옴


Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App)
}).$mount('#app');
