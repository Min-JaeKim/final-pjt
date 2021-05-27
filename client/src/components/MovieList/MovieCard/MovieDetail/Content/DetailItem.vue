<template>
  <div class="d-flex card text-center" id="card">
    <br>
    <h4>user</h4>
    <p>{{ review.username }}</p>
    <hr>
    <p>{{ review.content }}</p>
    <hr>
    <button @click="doChange">수정</button>
    <div v-if="change">
      <input type="text" @keyup.enter="updateReview(review)" v-model="content">
    </div>
    <button @click="deleteReview(review)">삭제</button>
    <div>
      <b-button v-b-toggle.sidebar-variant>댓글보기</b-button>
      <b-sidebar id="sidebar-variant" title="댓글" bg-variant="dark" text-variant="light" shadow>
        <div class="px-3 py-2">
          <p>
            Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis
            in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.
          </p>
          <b-img src="https://picsum.photos/500/500/?image=54" fluid thumbnail></b-img>
        </div>
      </b-sidebar>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DetailItem',
  props: {
    review: {
      type: Object,
    }
  },
  data: function () {
    return {
      change: false,
      content: ''
    }
  },
  methods: {
    doChange: function () {
      this.change = !this.change
      console.log(this.change)
    },
    updateReview: function (review) {
      const updated = {
        ...review,
        content: this.content
      }
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/movies/reviews/${review.id}/`,
        data: updated,
        headers: this.$store.state.setToken()
      })
        .then((res) => {
          console.log(res)
          this.$emit('review-change')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteReview: function (review) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/reviews/${review.id}/`,
        headers: this.$store.state.setToken()
      })
        .then((res) => {
          console.log(res)
          this.$emit('review-change')
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>
  #card {
    height: 95%;
    width: 18%;
  }
  #sidebar-variant {
    background-color: #29052C;
    color: white;
  }
</style>