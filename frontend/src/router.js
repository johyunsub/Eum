import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from './views/Home';
import Dogs from './views/DogsPage';
import Dbti from './views/DbtiPage';

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
