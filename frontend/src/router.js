import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from './views/Home';
import Dogs from './views/Dogs';
import Dbti from './views/Dbti';

Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/dogs',
      component: Dogs,
    },
    {
      path: '/dbti',
      component: Dbti,
    },
  ],
});

export default router;
