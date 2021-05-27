<template>
  <div class="login d-flex card justify-content-center">
    <br>
    <h1>Login</h1>
    <br>
    <br>
    <div class="d-flex justify-content-around">
      <label for="username">아이디</label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <br>
    <br>
    <div class="d-flex justify-content-around align-items-center">
      <label for="password">비밀번호</label>
      <input type="password" id="password" v-model="credentials.password" @keyup.enter="login">
    </div>
    <br>
    <br>
    <button class="btn" @click="login" style="">로그인</button>
    <br>
    <br>
  </div>
</template>

<script>
import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://localhost:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
      .then(res => {
        // console.log(res)
        localStorage.setItem('jwt', res.data.token)
        this.$emit('login')
        this.$router.push({ name: 'Home' })
        this.$store.dispatch('createUsername', this.credentials.username)
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
  .login {
    top: 180px !important;
    width: 33.3%;
    height: 33.3%;
    left: 33.3%;
    right: 33.3%;
    border: 10px solid rgb(162, 48, 255) !important;
    border-radius: 2rem !important;
  }
</style>
