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
    user_rate: [],
    listId: null,
    isClicked: null,
    favoratieGenre: [],
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
    },
    // 여기는 data값이 뭐가 들어올 지 모르기 때문에 내가 수정해줘야함.
    CREATE_RATE: function (state, data){
      state.user_rate.push(data)
    },
    CREATE_FAV_GENRE: function (state, data){
      state.favoratieGenre = data
    },
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
    },
    createRate: function ( { commit }, rate ){
      // this.$store.state -> this로 바뀔 수 있는지 추후 확인하기.
      axios ({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.$store.state.username}/rating/`,
        data: {
          'rate': rate,
          'movie': this.$store.state.movie,
        },
        headers: this.$store.state.setToken,
      })
        .then(res => {
          commit('CREATE_RATE', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    createFavGenre: function ( { commit }, data) {
      commit('CREATE_FAV_GENRE', data)
    },
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
