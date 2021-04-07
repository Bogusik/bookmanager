import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'

Vue.use(Vuex)

export default new Vuex.Store({
  state: () => {
    return {
      user: null,
      books: []
    }
  },
  mutations: {
    setUser (state, user) {
      state.user = user
    },
    setBooks (state, books) {
      state.books = books
    }
  },
  actions: {
    async LogIn ({ dispatch }, User) {
      const resp = await Vue.axios.post('/users/auth/', User) 
      localStorage.setItem('token', resp.data.token)
      dispatch('getUser').then(() => router.push('/'))
    },
    async getUser ({ commit }) {
      const resp = await Vue.axios.get('/users/me/', { headers: { Authorization: "JWT " + localStorage.getItem('token') }})
      if (resp.status == 200) {
        commit('setUser', resp.data)
      } else {
        localStorage.removeItem('token')
        router.push('/login')
      }
    },
    getBooks ({ commit }) {
      const conf = { headers: { Authorization: "JWT " + localStorage.getItem('token') }}
      Vue.axios.get('/books/', conf).then((resp) => {
        commit('setBooks', resp.data)
      }).catch((e) => console.log(e))
    },
    removeBook ({ dispatch }, id) {
      const conf = { headers: { Authorization: "JWT " + localStorage.getItem('token') }}
      Vue.axios.delete(`/books/${id}/`, conf).then(
        () => dispatch('getBooks', id)
      ).catch(
        (e) => console.log(e)
      )
    }
  },
  modules: {
  }
})
