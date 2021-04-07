import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import store from '../store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/',
    name: 'Books',
    component: () => import('../views/Books.vue')
  },
  {
    path: '/edit/:id',
    name: 'EditBook',
    component: () => import('../views/EditBook.vue')
  },
  {
    path: '/add',
    name: 'AddBook',
    component: () => import('../views/AddBook.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: '/',
  routes
})

router.beforeEach(async (to, from, next) => {
  if (to.name !== 'Login' && localStorage.getItem('token')) {
    try {
      const resp = await Vue.axios.get('/users/me/', { headers: { Authorization: "JWT " + localStorage.getItem('token') }})
      if (resp.status == 200) {
        store.commit('setUser', resp.data)
        next()
      } else {
        localStorage.removeItem('token')
        next({ name: 'Login' })
      }
    } catch {
      localStorage.removeItem('token')
      next({ name: 'Login' })
    }
  } else {
    if (localStorage.getItem('token')) {
      localStorage.removeItem('token')
    }
    if (to.name === 'Login') {
      next()
    }
    next({ name: 'Login' })
  }
})


export default router
