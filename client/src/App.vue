<template>
  <div id="app">
    <b-navbar id="nav" toggleable="lg">
      <b-navbar-brand href="#">잼민</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-link :to="{ name: 'Home' }" class="px-2 text-decoration-none">Home</b-link>
          <b-link :to="{ name: 'Recom' }" class="px-2 text-decoration-none">추천작</b-link>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="d-flex justify-content-end">
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0 d-inline-blockp text-purple" type="submit">Search</b-button>

          <b-link :to="{ name: 'Signup' }" class="px-2 text-decoration-none">Signup</b-link>
          <b-link :to="{ name: 'Login' }" class="px-2 text-decoration-none">Login</b-link>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <router-view/>
  </div>
</template>

<script>

export default {
  name: 'Home',
  created: function() {
    this.$store.dispatch('loadData')
    this.$store.dispatch('loadListData')
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* color: #2c3e50; */
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: rgb(172, 19, 146);
}

/* #nav a.router-link-exact-active {
  color: #42b983;
} */


</style>
