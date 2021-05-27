<template>
  <div>
    <h2 class="title"><span class="username">“{{ this.$store.state.username }}”</span>님을 위한 랜덤 추천작</h2>
    <br><br>
    <span v-if="select">
      <button @click="randomMovie">Pick!</button>
      <div v-if="clicked">
        <br>
        <h2><p>추천 영화 : {{ recMovie.title }}</p></h2>
        <img :src="`https://image.tmdb.org/t/p/w1280/${recMovie.backdrop_path}`" :alt="recMovie.title" style="object-fit: cover">
        <br><br>
        <p class="overview">줄거리 : {{ recMovie.overview }}</p>
      </div>
    </span>
    <span v-else>찜한 영화가 없거나 너무 적습니다.</span>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'Random',
  data: function () {
    return {
      clicked: null,
      recMovie: null,
      select: this.$store.state.favoratieGenre,
    }
  },
  methods: {
    randomMovie: function () {
      const allMovie = this.$store.state.movies
      const selectMovie = this.$store.state.favoratieGenre
      console.log(this.select)
      let recMovies = []
      for (let i=0; i < allMovie.length; i++) {
        for (let j=0; j < selectMovie.length; j++){
          if(allMovie[i].genre.split(',')[0] === selectMovie[0].num){
            recMovies.push({
              'title': allMovie[i].title,
              'backdrop_path': allMovie[i].backdrop_path,
              'overview': allMovie[i].overview
            })
            break
          }
        }
      }
      // this.recMovie = recMovies
      this.recMovie = _.sample(recMovies)
      this.clicked=true
    }
  }
}
</script>

<style>
  .title {
    color: white;
  }
  .username {
    color: #D38FFF;
  }
  .overview {
    color: white
  }
</style>