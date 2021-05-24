<template>
  <div>
    <h1>{{ movie.title }}</h1>
    <img :src="`https://image.tmdb.org/t/p/w200/${movie.poster_path}`" :alt="movie.title">
    <Basic/>
    <Detail :movie-id="movie.movie_id"/>
    <Rec/>
  </div>
</template>

<script>
import Basic from '@/components/MovieList/MovieCard/MovieDetail/Content/Basic' 
import Detail from '@/components/MovieList/MovieCard/MovieDetail/Content/Detail' 
import Rec from '@/components/MovieList/MovieCard/MovieDetail/Content/Rec' 

export default {
  name: 'Content',
  components: {
    Basic,
    Detail,
    Rec,
  },
  data: function () {
    return {
      movie: this.$store.state.movie
    }
  }
}
</script>

<style>

</style>