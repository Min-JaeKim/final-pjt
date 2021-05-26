<template>
  <li @click="selectReview">
    <span>{{ review.content }}</span>
    <!-- <span>{{ review.created_at }}</span> -->
    <button @click="updateReview">update</button>
    <button @click="deleteReview">X</button>
  </li>
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