<template>
  <div>
    <input type="text" v-model="reviewContent" @keyup.enter="createReview">
    <button @click="createReview">리뷰작성</button>
    <br>
    <DetailItem
    v-for="(review, idx) in reviews" 
    :key="idx"
    :review="review"
    />
  </div>
</template>

<script>
import axios from 'axios'
import DetailItem from '@/components/MovieList/MovieCard/MovieDetail/Content/DetailItem' 
export default {
  name: 'Detail',
  props: {
    movieId: {
      type: Number
    }
  },
  components: {
    DetailItem,
  },
  data: function() {
    return {
      reviewContent: null,
      reviews: [],
    }
  },
  methods: {
    getReviews: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.movieId}/review_list/`,
      })
        .then((res) => {
          this.reviews = res.data
          console.log(this.reviews)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    createReview: function () {
      // 로그인안되어 있을 때 리뷰 달지 못하게 막아야 한다.
      const createReview = {
        content: this.reviewContent,
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movieId}/review_create/`,
        data: createReview,
        headers: this.$store.state.setToken()
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created: function () {
    this.getReviews()
  }
}
</script>

<style>

</style>