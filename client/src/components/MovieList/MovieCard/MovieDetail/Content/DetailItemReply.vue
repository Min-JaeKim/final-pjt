<template>
  <div>
    <div >
      <p class="mb-0">{{ reply.content }}</p>
    </div>
    <div v-if="this.user_id === reply.user_id" class="mb-3">
      <button class="btn" style="color: white;" @click="doChange">수정</button>
      <button class="btn" style="color: white;" @click="deleteReply(reply)">삭제</button>
    </div>
    <div v-if="change">
      <input type="text" @keyup.enter="updateReply(reply)" v-model.trim="content">
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "DetailItemReply",
  props: {
    reply: {
      type: Object
    }
  },
  data: function () {
    return {
      change: false,
      content: this.reply.content,
      user_id: null,
    }
  },
  methods: {
    doChange: function () {
      this.change = !this.change
    },
    updateReply: function (reply) {
      const updated = {
        ...reply,
        content: this.content
      }
      console.log(reply)
      console.log(updated)
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/movies/replies/${reply.id}/`,
        data: updated,
        headers: this.$store.state.setToken()
      })
        .then((res) => {
          console.log(res)
          this.$emit('reply-change')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteReply: function (reply) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/replies/${reply.id}/`,
        headers: this.$store.state.setToken()
      })
        .then((res) => {
          console.log(res)
          this.$emit('reply-change')
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created: function () {
      axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/movies/reply_user/',
      headers: this.$store.state.setToken()
    })
      .then(res => {
        this.user_id = res.data.user_id
      })
      .catch(err => {
        console.log(err)
      })
    }
}
</script>

<style>
  .close {
    display: inline-block;
    font-weight: 400;
    line-height: 1.5;
    color: white;
    text-align: center;
    text-decoration: none;
    vertical-align: middle;
    cursor: pointer;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    background-color: transparent;
    border: 1px solid transparent;
    padding: 0.375rem 0.75rem;
    font-size: 1rem;
    border-radius: 0.25rem;
    transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  }
</style>