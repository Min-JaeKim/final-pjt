<template>
  <div>
    <MovieList
      v-for="(movieList, idx) in movieList"
      :key="idx"
      :movieList="movieList"
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
