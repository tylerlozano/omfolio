import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [

  {
    path: '/',
    name: 'Home',
    component: Home
  },


  {
    path: '/:id/:slug',
    name: 'BlogPost',
    props: true,
    component: () => import(/* webpackChunkName: "blogpost" */ '@/views/BlogPost.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior() {
    return { x: 0, y: 0 }
  }
})

export default router
