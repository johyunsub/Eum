import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from './views/Home';
import Dogs from './views/DogsPage';
import DogList from './views/DogListPage';
import DogDetail from './views/DogDetailPage';
import Dbti from './views/DbtiPage';
import Mdti from './views/MdtiPage';
import MdtiResult from './views/MdtiResultPage';
import MdtiStart from './views/MdtiStartPage';

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
      path: '/mdti',
      name: 'mdti',
      component: Mdti,
    },
    {
      path: '/mdtiResult',
      name: 'mdtiResult',
      component: MdtiResult,
    },
    {
      path: '/dbti',
      name: 'dbti',
      component: Dbti,
    },
    {
      path: '/mdtiStart',
      name: 'mdtiStart',
      component: MdtiStart,
    },
  ],
});

export default router;
