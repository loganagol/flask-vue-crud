import Vue from 'vue';
import VueRouter from 'vue-router';
import MyPing from '../components/MyPing.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/myping',
    name: 'MyPing',
    component: MyPing,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
