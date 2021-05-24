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
  props: {
    movieId: {
      type: Number
    }
  },
  data: function() {
    return {
      reviewContent: null,
    }
  },
  methods: {
    createReview: function () {
      const request = {
        content: this.reviewContent,
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movieId}/review_create/`,
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
  created: function () {
    axios ({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${this.movieId}/review_list/`,
    })
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
  },
}
</script>

<style>

</style>