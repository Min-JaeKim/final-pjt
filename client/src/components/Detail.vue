<template>
  <div>
    <input type="text" v-model="reviewContent" @keyup.enter="createReview">
    <button @click="createReview"></button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Detail',
  data: function() {
    return {
      reviewContent: null,
    }
  },
  created: function () {
    console.log(this.movieId)
    axios ({
      method: 'get',
      url: `http://localhost:8000/movies/${this.movieId}/review_list/`,
    })
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
  },
  methods: {
    createReview: function () {
      const request = {
        content: this.reviewContent,
      }
      axios({
        method: 'post',
        url: `http://localhost:8000/movies/${this.movieId}/review_create/`,
        data: request,
        headers: this.$store.state.setToken()
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
    movieId: function () {
      return this.$store.state.movieId
    }
  }
}
</script>

<style>

</style>