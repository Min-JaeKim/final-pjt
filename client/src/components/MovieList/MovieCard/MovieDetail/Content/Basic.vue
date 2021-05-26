<template>
  <div>
    <div class="left">
      <h3>{{ movie.title }}</h3>
      <p>{{ movie.overview }}</p>
      <button @click="likeMovie" v-if="liked">좋아요 취소</button>
      <button @click="likeMovie" v-else>좋아요</button>
      <b-form-rating v-model="value" color="indigo" class="mb-2">
        <button></button>
      </b-form-rating>
    </div>
    <div class="right">
      <!-- <img class="basic_layered"> -->
      <img class="basic" :src="`https://image.tmdb.org/t/p/w200/${movie.poster_path}`" :alt="movie.title">
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Basic',
  data: function () {
    return {
      liked: null,
      value: null,
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
    position: absolute;
    display: inline-block;
    right: 50%;
    width: 50%;
    height: 720px;
  }
  .right {
    position: absolute;
    display: inline-block;
    left: 50%;
    width: 50%;
    height: 720px;
  }
  img.basic {
    height: 720px; 
    object-fit: cover;
  }
</style>