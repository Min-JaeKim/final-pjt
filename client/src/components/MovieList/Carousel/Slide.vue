<template>
  <div>
    <div id="temp" v-b-hover="hoverHandler" :style="width">
      <img 
        :src="`https://image.tmdb.org/t/p/w500/${movie.backdrop_path}`" 
        :alt="`${movie.title}`"
      >
    </div>
  </div>
</template>

<script>
export default {
  nmae: 'Slide',
  props: {
    movieId: Number,
    top: null,
  },
  data: function () {
    return {
      width: "width: 19%"
    }
  },
  methods: {
    selectMovie: function () {
      this.$store.dispatch('selectMovie', this.movie)
    },
    hoverHandler(isHovered) {
      if (isHovered) {
        this.isViewed = isHovered
        this.selectMovie()
        this.width = "width: 326px"
        console.log(isHovered)
      } else {
        this.isViewed = false
        this.width = "width: 19%"
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
  img {
    width: 100%;
  }
  #temp {
    position: relative;
    top: 18%;
  }
  #temp:hover {
    top: 0%;
    width: 326px;
    transition: all 1s ease-in-out;
}
</style>