<template>
  <div>
    <br>
    <br>
    <h3>{{item.title}}</h3>
  </div>
</template>

<script>

export default {
  name: 'RecListItem',
  props: {
    item: {
      type: Object
    }
  }
}
</script>

<style>

</style>