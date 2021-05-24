<template>
  <div>
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

</style>