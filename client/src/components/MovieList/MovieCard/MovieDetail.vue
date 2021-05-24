<template>
  <div>
    <h1>aksfldjfkalsjjlsfajlkass</h1>
    <b-button v-b-toggle.my-collapse>Toggle Collapse</b-button>
    <b-collapse id="my-collapse">
      <b-card title="Collapsible card">
      <Content />
      </b-card>
    </b-collapse>
  </div>
</template>

<script>
import Content from '@/components/MovieList/MovieCard/MovieDetail/Content'

export default {
  name: 'MovieDetail',
  components: {
    Content
  },
}
</script>

<style> 

</style>
