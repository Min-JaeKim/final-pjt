<template>
  <div class="signup">
    <h1>Signup</h1>
    <div class="username">
      <label for="username">사용자 이름:</label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div class="password">
      <label for="password">비밀번호:                 </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <div class="confirmpassword">
      <label for="passwordConfirmation">비밀번호 확인:                 </label>
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation">
    </div>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials:{
        username: null,
        password: null,
        passwordConfirmation: null,

      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://localhost:8000/accounts/signup/',
        data: this.credentials,
      })
      .then(res => {
        console.log(res)
        this.$router.push({ name: 'Login' })
      })
      .catch(err =>{
        console.log(err)
        // 동일한 아이디로 가입을 했을 때, 400err가 뜨는 것을 확인.
      })
    }
  }
}
</script>

<style>
  .signup {
    color: white;
  }
  /* .username {
    color: white;
  }
  .password {
    color: white;
  }
  .confirmpassword {
    color: white;
  } */
</style>