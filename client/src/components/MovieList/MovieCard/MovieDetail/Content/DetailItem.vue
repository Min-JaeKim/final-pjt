<template>
  <div @click="selectReview">
    <span>{{ review.content }}</span>
    <button @click="updateReview">update</button>
    <button @click="deleteReview">X</button>
  </div>
</template>

<script>
export default {
  name: 'DetailItem',
  props: {
    review: {
      type: Object,
    }
  },
  methods: {
    selectReview: function () {
    },
    updateReview: function () {

    },
    deleteReview: function () {

    }
  }
}
</script>

<style>

</style>