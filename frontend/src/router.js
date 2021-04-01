import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from './views/Home';
import Dogs from './views/DogsPage';
import DogList from './views/DogListPage';
import DogDetail from './views/DogDetailPage';
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
      name: 'dogs',
      component: Dogs,
    },
    {
      name: 'dogList',
      path: '/dogList',
      component: DogList,
    },
    {
      name: 'dogDetail',
      path: '/dogDetail',
      component: DogDetail,
    },
    {
      path: '/dbti',
      name: 'dbti',
      component: Dbti,
    },
  ],
});

export default router;
