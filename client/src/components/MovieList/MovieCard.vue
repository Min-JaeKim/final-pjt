<template>
  <div class="my-4" v-b-hover="hoverHandler">
    <h3>{{ movie.title }}</h3>
    <img 
      :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" 
      :alt="`${movie.title}`"
    >
    <p>{{ movie.overview }}</p>
    <MovieDetail v-if="isViewed"/>
  </div>
</template>

<script>
import MovieDetail from "@/components/MovieList/MovieCard/MovieDetail"

export default {
  name: 'MovieCard',
  props: {
    movieId: {
      type: Number,
    }
  },
  components: {
    MovieDetail,
  },
    data: function () {
    return {
      isViewed: false,
    }
  },
  methods: {
    selectMovie: function () {
      this.$store.dispatch('selectMovie', this.movie)
    },
    hoverHandler(isHovered) {
      if (isHovered) {
        console.log(isHovered)
        this.isViewed = isHovered
        this.selectMovie()
      } else {
        this.isViewed = false
      }
    }
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

</style>