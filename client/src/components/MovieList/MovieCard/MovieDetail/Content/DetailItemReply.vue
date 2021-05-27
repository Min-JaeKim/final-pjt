<template>
  <div>
    <div class="d-flex justify-content-between">
      <p>{{ reply.content }}</p>
      <div>
        <button @click="doChange">수정</button>
        <button @click="deleteReply(reply)">삭제</button>
      </div>
    </div>
    <div v-if="change">
      <input type="text" @keyup.enter="updateReply(reply)" v-model="content">
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
      content: '',
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
    }
  }
}
</script>

<style>

</style>