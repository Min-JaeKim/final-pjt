<template>
  <div>
    <h1>Movie List</h1>
    <MyListForm/>
    <MyList 
      v-for="(movie, idx) in movieList" 
      :key="idx" 
      :movie="movie"
    />
  </div>
</template>

<script>
import MyList from '@/components/MyList'
import MyListForm from '@/components/MyListForm'
export default {
  name: 'MyMovieList',
  components: {
    MyList,
    MyListForm,
  },
  computed: {
    movieList: function (){
      return this.$store.state.trending_movies
    },
  }
}
</script>

<style>

</style>