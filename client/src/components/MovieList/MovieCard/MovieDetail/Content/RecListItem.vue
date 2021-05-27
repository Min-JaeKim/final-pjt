<template>
  <div id="item">
    <br>
    <br>
    <h3>{{item.title}}</h3>
    <img :src="`https://image.tmdb.org/t/p/w500/${item.backdrop_path}`" :alt="item.title" style="object-fit: cover">
    <!-- <iframe src="" frameborder="0"></iframe> -->
  </div>
</template>

<script>
import axios from 'axios'

// const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_YOUTUBE_KEY


export default {
  name: 'RecListItem',
  props: {
    item: {
      type: Object
    }
  },
  created: function () {
    const TMDB_KEY = process.env.VUE_APP_TMDB_KEY
    const TMDB_URL = `https://api.themoviedb.org/3/movie/${this.item.id}/videos?api_key=${TMDB_KEY}&language=ko-KR`
    console.log(TMDB_KEY)
    console.log(API_KEY)
    axios({
      method: 'get',
      url: TMDB_URL,
    })
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style scoped>
  #item {
    position: relative;
    width: 33.3%;
    height: 100%;
    display: inline-block;
  }
</style>