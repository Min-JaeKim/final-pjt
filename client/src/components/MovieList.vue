<template>
  <b-media>
    <h3>{{ movieList[0].description }}</h3>
    <MovieCard 
      v-for="(movieId, idx) in movieList"
      :key="idx"
      :movieId="movieId"
      @is-modal="isModal"
    />
    <MovieDetail v-if="isModalViewed" @close-modal="isModalViewed = false"/>
  </b-media>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import MovieDetail from "@/components/MovieDetail"

export default {
  name: 'MovieList',
  props: {
    movieList: {
      type: Array,
    }
  },
  components: {
    MovieCard,
    MovieDetail,
  },
  data: function () {
    return {
      isModalViewed: false,
    }
  },
  methods: {
    isModal: function () {
      this.isModalViewed = !this.isModalViewed
    }
  },
}
</script>

<style>

</style>