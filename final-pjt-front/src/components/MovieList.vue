<template>
  <div id="carousel">
    <div style="width: 40%">
      <h4 id="title">{{ movieList[0].description }}</h4>
    </div>
    <Carousel :carousel="carousel" id="carousel-list" :listId="listId" style="position: relative;"/>

    <!-- <MovieCard 
      v-for="(movie, idx) in movieList"
      :key="idx"
      :movieId="movie.movie_id"
    /> -->
    <div>      
      <Content
        id="content"
        v-if=" this.$store.state.isClicked && this.$store.state.listId == listId"
        style="position: relative; z-index: 2; transition: z-index 0.5s"
      />
    </div>
    <div id="blank"></div>
  </div>
</template>

<script>
// import MovieCard from '@/components/MovieList/MovieCard'
import Carousel from '@/components/MovieList/Carousel'
import Content from '@/components/MovieList/MovieCard/MovieDetail/Content'


export default {
  name: 'MovieList',
  props: {
    movieList: {
      type: Array,
    },
    listId: {
      type: Number
    }
  },
  components: {
    // MovieCard,
    Carousel,
    Content,
  },
  computed: {
    carousel: function () {
      const temp = []
      let temp2 = []
      let idx = 0
      while (idx < this.movieList.length) {
        if ((idx != 0 && idx % 5 == 0) || idx == this.movieList.length - 1) {
          temp.push(temp2)
          temp2 = []
        }
        temp2.push(this.movieList[idx])
        idx += 1
      }
      return temp
    }
  }
}
</script>

<style scoped>
  #title {
    font-family: SEBANG_Gothic_Bold;
    color: white;
  }
  #carousel {
    width: 100%;
    height: 12.5%;
  }
  #title {
    width: 100%;
    height: 15%;
  }
  #carousel-list {
    width: 100%;
    height: 75%;
    
  }
  #blank {
    width: 100%;
    height: 10%;
    
  }
  #content {
    height: 800px;
    background-color: #39343a;
    z-index: 0;
  }
</style>