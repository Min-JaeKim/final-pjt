<template>
  <div>
    <img 
      :src="`https://image.tmdb.org/t/p/w500/${movie.backdrop_path}`" 
      :alt="`${movie.title}`"
    >
  </div>
</template>

<script>
export default {
  nmae: 'Slide',
  props: {
    movieId: Object,
  },
  computed: {
    movie: function () {
      const temp = this.$store.state.movies.filter(movie => {
        return movie.movie_id === this.movieId
      })[0]
      return temp
    }
  }
}
</script>

<style>
 img {
   width: 100%;
 }
</style>