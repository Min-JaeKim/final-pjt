<template>
  <div>
    <div class="left">

    </div>
    <div class="right">
      <img :src="`https://image.tmdb.org/t/p/w200/${movie.poster_path}`" :alt="movie.title" style="object-fit: none; width: 35%;">
    </div>
    <p>{{ movie.overview }}</p>
    <button @click="likeMovie" v-if="liked">좋아요 취소</button>
    <button @click="likeMovie" v-else>좋아요</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Basic',
  data: function () {
    return {
      liked: null,
    }
  },
  methods: {
    likeMovie: function () {
      const token = this.$store.state.setToken()
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movie.movie_id}/likes/`,
        headers: token,
      })
      .then(res => {
        this.liked = res.data.liked
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  computed: {
    movie: function () {
      return this.$store.state.movie
    }
  }
}
</script>

<style>
  .left {
    display: inline-block;
    width: 50%;
    height: 100%;
  }
  .right {
    display: inline-block;
    width: 50%;
    height: 100%;
  }
  img {
    object-fit: cover; 
    position: relative; 
    background: linear-gradient(to right, black, white);
  }
</style>