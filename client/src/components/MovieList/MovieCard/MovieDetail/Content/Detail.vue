<template>
  <div>
    <div class="left">
      <br>
      <br>
      <br>
      <br>
      <br>
      <h1>Review</h1>
      <br>
      <input type="text" v-model="reviewContent" @keyup.enter="createReview">
      <button @click="createReview">리뷰작성</button>
    </div>
    <div class="right" :style="`background: linear-gradient(215deg, transparent 10%, black), url('https://image.tmdb.org/t/p/w500/${movie.backdrop_path}'); background-size: 100% auto !important; opacity:0.3;`">
    </div>
    <div class="detail-list d-flex flex-wrap justify-content-around">
      <DetailItem
        v-for="(review, idx) in reviews" 
        :key="idx"
        :review="review"
        @review-change="reviewChange"
      />
    </div>
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
          this.reviews = this.getReviews()
        })
        .catch(err => {
          console.log(err)
        })
    },
    reviewChange: function () {
      this.reviews = this.getReviews()
    }
  },
  computed: {
    movie: function () {
      return this.$store.state.movie
    },
  },
  created: function () {
    this.getReviews()
  }
}
</script>

<style scoped>
  .left {
    position: absolute;
    display: inline-block;
    right: 70%;
    width: 30%;
    height: 300px;
    z-index: 1;
  }
  .right {
    position: absolute;
    display: inline-block;
    left: 0%;
    width: 100%;
    height: 300px;
  }
  .detail-list {
    position: relative;
    top: 330px;
    width: 94%;
    height: 350px;
    left: 3%;
    right: 3%;
}
</style>