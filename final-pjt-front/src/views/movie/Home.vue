<template>
  <div id="list">
    <h1 style="color: white">Welcome to Just Movie</h1>
    <br>
    <b-carousel
      id="carousel-fade"
      :interval="5000"
      style="text-shadow: 0px 0px 2px #000"
      fade
      indicators
      img-width="1024"
      img-height="480"
    >
      <b-carousel-slide
        v-for="(trending, idx) in trendings"
        :key="idx"
        :img-src="`https://image.tmdb.org/t/p/w1280/${trending.backdrop_path}`"
      >

      </b-carousel-slide>
    </b-carousel>
    <br><br>
    <h2 style="color: white">JM Series!</h2>
    <br><br>
    <MovieList
      v-for="(movieList, idx) in movieList"
      :key="idx"
      :movieList="movieList"
      :listId="idx"
    />
  </div>
</template>

<script>
import MovieList from "@/components/MovieList"
import axios from 'axios'

const TMDB_API_KEY = process.env.VUE_APP_TMDB_KEY
const TMDB_API_URL = `https://api.themoviedb.org/3/movie/now_playing?api_key=${TMDB_API_KEY}&language=ko-KR&page=1`

export default {
  name: 'Home',
  components: {
    MovieList,
  },
  data: function () {
    return {
      trendings: []
    }
  },
  computed: {
    movieList: function () {
      return this.$store.state.movieList
    }
  },
  created: function () {
    axios({
      method: 'get',
      url: TMDB_API_URL
    }).
      then(res =>{
        this.trendings = res.data.results
      })
  }
}
</script>

<style scoped>
  #list {
    height: 2400px;
  }
</style>
