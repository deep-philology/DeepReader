import Vue from 'vue';
import Router from 'vue-router';
import CTSReader from '@/cts/components/Reader';
import MorphGNTReader from '@/morphgnt/components/Reader';
import CiteServicesReader from '@/cite-services/components/Reader';
import Homepage from '@/components/Homepage';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Homepage',
      component: Homepage,
    },
    {
      path: '/cts',
      name: 'CTSReader',
      component: CTSReader,
    },
    {
      path: '/morphgnt',
      name: 'MorphGNTReader',
      component: MorphGNTReader,
    },
    {
      path: '/cite-services',
      name: 'CiteServicesReader',
      component: CiteServicesReader,
    },
  ],
});
