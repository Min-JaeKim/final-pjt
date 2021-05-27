<template>
  <div>
    <div class="left">
      <div class="p-5 d-flex allign-items-center flex-column" style="height: 100%">
        <div class="justify-content-between">
          <h3>{{ movie.title }}</h3>
          <div v-if="this.$store.state.username">
            <p v-if="liked">
              좋아요 <font-awesome-icon :icon="['fas','heart']" @click="likeMovie"/>
            </p>
            <p v-else>
              싫어요 <font-awesome-icon :icon="['far','heart']" @click="likeMovie"/>
            </p>
          </div>
        </div>
        <br><br>
        <h4>"{{ movie.tagline }}"</h4>
        <br><br>
        <p style="color: white; text-align: left">{{ movie.overview }}</p>
        <br><br>
        <div v-if="this.$store.state.username">
          <br>
          <br>
          <h3>몇 점 주실래요?</h3>
          <br><br><br>
          <b-form-rating v-model="value" color="indigo" class="mb-2" @change="onClick">
          <button></button>
          </b-form-rating>        
        </div>
      </div>
    </div>
    <div class="right" :style="`background: linear-gradient(to left, transparent, black), url('https://image.tmdb.org/t/p/w1280/${movie.poster_path}'); background-size: 100% auto;`">
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
      token: this.$store.state.setToken()
    }
  },
  methods: {
    likeMovie: function () {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movie.movie_id}/likes/`,
        headers: this.token,
      })
      .then(res => {
        this.liked = res.data.liked
      })
      .catch(err => {
        console.log(err)
      })
    },
    onClick: function () {
        const value = {
          rate: this.value
        }
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/${this.movie.movie_id}/rating/`,
          data: value,
          headers: this.token
        })
          .then(res => {
            console.log(res)
          })
          .catch(err => {
            console.log(err)
          })
    }
  },
  computed: {
    movie: function () {
      return this.$store.state.movie
    },
    username: function () {
      return this.$store.state.username
    },
  }
}
</script>

<style scoped>
  .left {
    position: absolute;
    display: inline-block;
    right: 50%;
    width: 50%;
    height: 720px;
    color: white
  }
  .right {
    position: absolute;
    display: inline-block;
    left: 50%;
    width: 50%;
    height: 720px;
  }
</style>