import { createRouter, createWebHistory } from 'vue-router';
import FstPage from '../pages/FstPage.vue';
import SecPage from '../pages/SecPage.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'first-page',
      component: FstPage,
    },
    {
      path: '/second-page',
      name: 'second-page',
      component: SecPage,
    }
  ],
})

export default router;
