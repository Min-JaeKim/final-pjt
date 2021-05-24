<template>
  <div>
    <input type="text" @keyup.enter="addMovie" v-model="query">
    <button @click="addMovie">add</button>
  </div>
</template>

<script>
export default {
  name: 'MyListForm',
  data: function () {
    return {
      query: '',
    }
  },
  methods: {
    addMovie: function () {
      // this.$emit('addMovie', this.query)
      this.$store.dispatch('addMovie', this.query)
    }
  }
}
</script>

<style>

</style>