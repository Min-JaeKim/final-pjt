<template>
  <div>
    <h3>{{ movieList[0].description }}</h3>
    
    <MovieCard 
      v-for="(movie, idx) in movieList"
      :key="idx"
      :movieId="movie.movie_id"
    />
  </div>
</template>

<script>
import MovieCard from '@/components/MovieList/MovieCard/'

export default {
  name: 'MovieList',
  props: {
    movieList: {
      type: Array,
    }
  },
  components: {
    MovieCard,
  },
}
</script>

<style>

</style>