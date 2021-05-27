<template>
  <div id="app">
    <b-navbar id="nav" toggleable="lg">
      <b-navbar-brand :to="{ name: 'Home' }" class="p-2">JM</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-link :to="{ name: 'Home' }" class="px-2 text-decoration-none">Home</b-link>
            <b-link :to="{ name: 'Recom' }" class="px-2 text-decoration-none">추천작</b-link>
          </b-navbar-nav>

          <b-navbar-nav class="d-flex justify-content-end">
            <span v-if="isLogin">
              <b-link :to="{ name: 'MyPage' }" class="px-2 text-decoration-none">MyPage</b-link>
              <b-link :to="{ name: 'Logout' }" class="px-2 text-decoration-none" @click.native="logout">Logout</b-link>
            </span>
            <span v-else>
              <b-link :to="{ name: 'Signup' }" class="px-2 text-decoration-none">Signup</b-link>
              <b-link :to="{ name: 'Login' }" class="px-2 text-decoration-none">Login</b-link>
            </span>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <router-view @login="isLogin = true"/>
  </div>
</template>

<script>

export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Home' })
    }
  },
  created: function() {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
    this.$store.dispatch('loadData')
    this.$store.dispatch('loadListData')
  },
}
</script>


<style>
  @font-face {
      font-family: 'SEBANG_Gothic_Bold';
      src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2104@1.0/SEBANG_Gothic_Bold.woff') format('woff');
      font-weight: normal;
      font-style: normal;
  }
  div {
    color: rgb(162, 48, 255);
  }
  .navbar-brand {
    font-size: 3rem !important;
  }
  #nav {
    font-family: SEBANG_Gothic_Bold;
    font-size: 120.5%;
    padding: 30px;
  }
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    /* color: #2c3e50;*/
  }
  #nav a {
    font-weight: bold;
    color: rgb(162, 48, 255);
  }
  .navbar-toggler-icon {
    background-color: rgb(162, 48, 255);
  }
</style>
