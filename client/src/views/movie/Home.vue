<template>
  <ul class="list-unstyled">
    <MovieList
      v-for="(movieList, idx) in movieList"
      :key="idx"
      :movieList="movieList"
    />
  
  <!-- 클릭을 해야만 영화 내용을 보여줄 수 있다. -->
  <!-- <button @click="onMovies">눌러</button> -->

    <!-- <MovieCard 
      v-for="(movie, idx) in mList"
      :key="idx"
      :movie="movie"
      @is-modal="isModal"
    />
    <MovieDetail v-if="isModalViewed" @close-modal="isModalViewed = false"/> -->
      <!-- <Content msg="Hello Vue in CodeSandbox!"/>
    </MovieDetail> -->
  </ul>
</template>

<script>
// @ is an alias to /src
// import MovieCard from '@/components/MovieCard'
// import MovieDetail from "@/components/MovieDetail"
import MovieList from "@/components/MovieList"

export default {
  name: 'Home',
  components: {
    // MovieCard,
    // MovieDetail,
    MovieList,
  },
  // data: function () {
  //   return {
  //     isModalViewed: false,
  //   }
  // },
  // methods: {
  //   isModal: function () {
  //     this.isModalViewed = !this.isModalViewed
  //   }
  // },
  computed: {
    // mList: function () {
    //   return this.$store.state.movies
    // },
    movieList: function () {
      return this.$store.state.movieList
    }
  }
}
</script>
