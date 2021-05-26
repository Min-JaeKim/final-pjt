<template>
  <div :style="width">
    <div id="temp" v-b-hover="hoverHandler">
      <img 
        :src="`https://image.tmdb.org/t/p/w500/${movie.backdrop_path}`" 
        :alt="`${movie.title}`"
      >
      <b-button v-if="isViewed" v-b-toggle.my-collapse @click="onClick">Toggle Collapse</b-button>
      <!-- <Content v-if="isClicked"/> -->
    </div>
  </div>
</template>

<script>
// import Content from '@/components/MovieList/MovieCard/MovieDetail/Content'

export default {
  nmae: 'Slide',
  props: {
    movieId: {
      type: Number,
    },
    top: {
      type: null,
    },
    listId: {
      type: Number,
    }
  },
  components: {
    // Content
  },
  data: function () {
    return {
      width: "width: 19%",
      isViewed: false,
      isClicked: false,
      card: null,
    }
  },
  methods: {
    selectMovie: function () {
      this.$store.dispatch('selectMovie', this.movie)
    },
    hoverHandler(isHovered) {
      if (isHovered) {
        this.isViewed = isHovered        
        this.width = "width: 326px"
      } else {
        this.isViewed = false
        this.width = "width: 19%"
      }
    },
    onClick() {
      this.selectMovie()
      this.isClicked = !this.isClicked
      this.$store.state.isClicked = !this.$store.state.isClicked
      this.$store.state.listId = this.listId
      if (this.isClicked) {
        this.card = "position: absolute; width:500px; height:800px; z-index: 3;"
      } else {
        this.card = null
      }
    }
  },
  computed: {
    movie: function () {
      const temp = this.$store.state.movies.filter(movie => {
        return movie.movie_id === this.movieId
      })[0]
      return temp
    },
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
    transition: all 0.3s ease-in-out;
}
</style>