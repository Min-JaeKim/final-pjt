import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/movie/Home.vue'
import Random from '../views/movie/Random.vue'
import MyMovieList from '../views/movie/MyMovieList.vue'
import Signup from '../views/accounts/Signup'
import Login from '../views/accounts/Login'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movie/',
    name: 'Home',
    component: Home
  },
  {
    path: '/movie/random',
    name: 'Random',
    component: Random,
  },
  {
    path: '/movie/mymovielist',
    name: 'MyMovieList',
    component: MyMovieList,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
