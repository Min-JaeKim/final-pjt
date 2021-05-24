<template>
  <div>
    <h3>{{ movie.title }}</h3>
    <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" :alt="`${movie.title}`">
  </div>
</template>

<script>
export default {
  name: 'MyList',
  props: {
    movie: {
      type: Object,
    }
  }
}
</script>

<style>

</style>