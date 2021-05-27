<template>
  <div class="d-flex card text-center" id="card">
    <br>
    <h4>user</h4>
    <p>{{ review.username }}</p>
    <hr>
    <p>{{ review.content }}</p>
    <hr>
    <div v-if="user_id === review.user_id">
      <button class="btn" @click="doChange">수정</button>
      <div v-if="change">
        <input type="text" @keyup.enter="updateReview(review)" v-model.trim="content">
      </div>
      <br>
      <button class="btn" @click="deleteReview(review)">삭제</button>
    </div>
    <div>
      <b-button v-b-toggle.sidebar-variant>댓글보기</b-button>
      <b-sidebar id="sidebar-variant" title="댓글" bg-variant="dark" text-variant="light" shadow>
        <div class="px-3 py-2">
          <input type="text" v-model.trim="replyContent" @keyup.enter="createReply">
          <button class="btn" style="color: white; display: inline-block" @click="createReply">댓글작성</button>
          <hr>
          <br>
          <DetailItemReply
            v-for="(reply, idx) in replies"
            :key="idx"
            :reply="reply"
            @reply-change="replyChange"
          />
          <b-img :src="`https://image.tmdb.org/t/p/w500/${this.$store.state.movie.poster_path}`" fluid thumbnail></b-img>
        </div>
      </b-sidebar>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import DetailItemReply from '@/components/MovieList/MovieCard/MovieDetail/Content/DetailItemReply' 

export default {
  name: 'DetailItem',
  props: {
    review: {
      type: Object,
    }
  },
  components: {
    DetailItemReply,
  },
  data: function () {
    return {
      change: false,
      content: this.review.content,
      replies: [],
      replyContent: null,
      user_id: null,
    }
  },
  methods: {
    getReplies: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/reviews/${this.review.id}/reply_list/`,
      })
        .then(res => {
          this.replies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    createReply: function () {
      const createReply = {
          content: this.replyContent
        }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/reviews/${this.review.id}/reply_create/`,
        data: createReply,
        headers: this.$store.state.setToken()
      })
        .then(res => {
          console.log(res)
          this.replyContent = ''
          this.replies = this.getReplies()
        })
        .catch(err => {
          console.log(err)
        })
    },
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
    },
    replyChange: function () {
      this.replies = this.getReplies()
    }
  },
  created: function () {
    this.getReplies()
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/movies/review_user/',
      headers: this.$store.state.setToken()
    })
      .then(res => {
        this.user_id = res.data.user_id
        console.log(this.review)
      })
      .catch(err => {
        console.log(err)
      })
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