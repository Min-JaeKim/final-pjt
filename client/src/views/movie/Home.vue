<template>
  <div id="list">
    <MovieList
      v-for="(movieList, idx) in movieList"
      :key="idx"
      :movieList="movieList"
      :listId="idx"
    />
  </div>
</template>

<script>
import MovieList from "@/components/MovieList"

export default {
  name: 'Home',
  components: {
    MovieList,
  },
  computed: {
    movieList: function () {
      return this.$store.state.movieList
    }
  }
}
</script>

<style scoped>
  #list {
    height: 2400px;
  }
</style>
