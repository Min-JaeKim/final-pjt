import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios'
import createPersistedState from "vuex-persistedstate"
import axios from 'axios'


Vue.use(Vuex)

// const API_KEY = 'f361f3c50ed76f4dd96355b1957b3f29'
// const API_URL = `https://api.themoviedb.org/3/movie/now_playing?api_key=${API_KEY}&language=ko-kr&page=1`
// console.log(API_KEY)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    trending_movies: [],
    myMovieList: [],
    movieList: [],
    movies: [],
    movie: null,
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
          Authorization: `JWT ${token}`
      }
      return config
    },
    username: null,
  },
  mutations: {
    LOAD_DATA: function (state, data) {
      state.movies = data
    },
    LOAD_LIST_DATA: function (state, data) {
      state.movieList = data
    },
    SELECT_MOVIE: function (state, movie) {
      state.movie = movie
    },
    CREATE_USERNAME: function (state, username) {
      state.username = username
    }
  },
  actions: {
    selectMovie: function ( { commit }, movie) {
      commit('SELECT_MOVIE', movie)
    },
    addMovie: function ( { commit }, title) {
      const movie = this.state.movies.filter(movie => {
        return movie.title === title
      })
      commit('ADD_MOVIE', movie[0])
    },
    loadData: function ( { commit }) {
      axios ({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/',
      })
        .then(res => {
          commit('LOAD_DATA', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    loadListData: function ({ commit }) {
      axios ({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/movie_list/',
      })
        .then(res => {
          commit('LOAD_LIST_DATA', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    createUsername: function ( { commit }, username){
      commit('CREATE_USERNAME', username)
    }
  },
  // getters: {
  //   isModal: function (state) {
  //     if (state.movieId) {
  //       return state.movieId
  //     }
  //     return null
  //   }
  // },
  modules: {
  },
})
