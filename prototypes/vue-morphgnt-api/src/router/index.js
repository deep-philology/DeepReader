import Vue from 'vue';
import Router from 'vue-router';
import Reader from '@/components/Reader';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Reader',
      component: Reader,
    },
  ],
});
