<template>
  <b-media tag="li" class="my-4">
    <h3>{{ movie.title }}</h3>
    <img 
      :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" 
      :alt="`${movie.title}`"
      @click="selectMovie">
    <p>{{ movie.overview }}</p>
    <!-- <p>{{ movie }}</p> -->
  </b-media>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movieId: {
      type: Object,
    }
  }
  ,
  methods: {
    selectMovie: function () {
      this.$store.dispatch('selectMovie', this.movie)
      this.$emit('is-modal')
    }
  },
  computed: {
    movie: function () {
      const temp = this.$store.state.movies.filter(movie => {
        return movie.movie_id === this.movieId.movie_id
      })[0]
      return temp
    }
  }
}
</script>

<style>

</style>