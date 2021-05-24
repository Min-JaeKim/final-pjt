<template>
  <ul class="list-unstyled">
    <MovieList
      v-for="(movieList, idx) in movieList"
      :key="idx"
      :movieList="movieList"
    />
  </ul>
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
