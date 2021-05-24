<template>
  <div>
    <h2>영화 추천</h2>
    <button @click="randomMovie">Pick!</button>
    <p>추천 영화 : {{ selectMovie.title }}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'Random',
  data: function () {
    return {
      selectMovie: ''
    }
  },
  methods: {
    randomMovie: function () {
      const movies = this.$store.state.movies
      this.selectMovie = _.sample(movies)
    }
  }
}
</script>

<style>

</style>