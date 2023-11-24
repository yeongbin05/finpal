import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ExchangeRateView from '@/views/ExchangeRateView.vue'
import MapView from '@/views/MapView.vue'
import LogInView from '@/views/LogInView.vue'
import SignUpView from '@/views/SignUpView.vue'
import FinanceProductView from '@/views/FinanceProductView.vue'
import Ex2View from '@/views/Ex2View.vue'
import SavingView from '@/views/SavingView.vue'
import SnowView from '@/views/SnowView.vue'
import LandingView from '@/views/LandingView.vue'
import DetailView from '@/views/DetailView.vue'
import SavingDetailView from '@/views/SavingDetailView.vue'

import ArticleView from '@/views/ArticleView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleUpdateView from '@/views/ArticleUpdateView.vue'
import ProfileView from '@/views/ProfileView.vue'
import UserDataView from '@/views/UserDataView.vue'
import CartView from '@/views/CartView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'landing',
      component: LandingView
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path: '/exchangerate',
      name: 'ExchangeRate',
      component: ExchangeRateView
    },
    {
      path: '/map',
      name: 'Map',
      component: MapView
    },
  
    {
      path: '/login',
      name: 'LogIn',
      component: LogInView
    },
  
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUpView
    },
  
    {
      path: '/financeproduct/:page_pk',
      name: 'FinanceProduct',
      component: FinanceProductView
    },
    {
      path: '/detail/:id',
      name: 'detail',
      component: DetailView
    },
    {
      path: '/ex2',
      name: 'ex2',
      component: Ex2View
    },
    {
      path: '/savings/:page_pk',
      name: 'saving',
      component: SavingView
    },
    {
      path: '/snow',
      name: 'snow',
      component: SnowView
    },
    {
      path: '/saving/:id',
      name: 'savingdetail',
      component: SavingDetailView
    },
    {
      path: '/articles',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'ArticleDetailView',
      component: ArticleDetailView
    },
    {
      path: '/articles/create',
      name: 'ArticleCreateView',
      component: ArticleCreateView
    },
    {
      path: '/articles/update/:id',
      name: 'ArticleUpdateView',
      component: ArticleUpdateView
    },
    {
      path: '/profile',
      name: 'ProfileView',
      component: ProfileView
    },
    {
      path: '/userdata',
      name: 'UserdataView',
      component: UserDataView
    },
    {
      path: '/cart',
      name: 'CartView',
      component: CartView
    },
  ]
})

import { useRateStore } from '@/stores/rate'

router.beforeEach((to, from) => {
  const store = useRateStore()
  if (to.name === 'ArticleView' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogIn' }
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'ArticleView' }
  }
})

export default router
