<template>
  <div>
    <input type="text" v-model.trim="content" @keyup.enter="createReply">
    <button @click="createReply">댓글 쓰기</button>
    <br>
    <!-- <li v-for="(reply, idx) in replys" :key="idx">
        <p>{{ reply.content }}</p>
        <p>{{ reply.created_at }}</p>
        <button @click="updateReply">update</button>
        <button @click="deleteTodo">X</button>
      </li> -->
  </div>
</template>

<script>
export default {
  name="Review",
  props: {
    // 이거 꼭 detail에서 props 시켜 주나 확인할 것.
    movieId: {
      type: Number
    },
    reviewId: {
      type: Number
    }
  },
  data: function () {
    return {
      setToken: this.$store.state.setToken(),
      replys: [],
      content: null,
    }
  },
  methods: {
    getReplys: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.movieId}/review/${this.reviewId}/`,
      })
        .then((res) => {
          console.log(res)
          this.replys = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // deleteReview: function () {
    //   axios({
    //     method: 'delete',
    //     url: `http://127.0.0.1:8000/movies/${this.movieId}/review/${this.reviewId}/`,
    //     headers: this.setToken(),
    //   })
    //     .then((res) => {
    //       console.log(res)
    //       this.getTodos()
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    // },
    // updateReview: function (todo) {
    //   const todoItem = {
    //     ...todo,
    //     completed: !todo.completed
    //   }

    //   axios({
    //     method: 'put',
    //     url: `http://127.0.0.1:8000/todos/${todo.id}/`,
    //     data: todoItem,
    //     headers: this.setToken()
    //   })
    //     .then((res) => {
    //       console.log(res)
    //       todo.completed = !todo.completed
    //     })
    //   },
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getReplys()
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style>

</style>