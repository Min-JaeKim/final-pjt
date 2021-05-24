<template>
  <div>
    <h1>{{ movie.title }}</h1>
    <img :src="`https://image.tmdb.org/t/p/w200/${movie.poster_path}`" :alt="movie.title" class="d-inline">
    <Basic/>
    <Detail/>
    <Rec/>
  </div>
</template>

<script>
import Basic from '@/components/Basic' 
import Detail from '@/components/Detail' 
import Rec from '@/components/Rec' 

// import Vue from 'vue'
// import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

// Vue.use(BootstrapVue)
// // Optionally install the BootstrapVue icon components plugin
// Vue.use(IconsPlugin)

export default {
  name: 'Content',
  components: {
    Basic,
    Detail,
    Rec,
  },
  data: function () {
    return {
      movie: this.$store.state.movie,
    }
  },
}
</script>

<style>

</style>