<template>
  <b-carousel
    ref="myCarousel"
    id="carousel-1"
    :interval="1000000"
    background="#000000"
    style="text-shadow: 1px 1px 2px #333;"
  >

    <a href="#" role="button" aria-controls="carousel-1___BV_inner_" class="carousel-control-prev" style="width: 5%;" @click="prev">
      <span aria-hidden="true" class="carousel-control-prev-icon"></span>
    </a>
    <a href="#" role="button" aria-controls="carousel-1___BV_inner_" class="carousel-control-next" style="width: 5%;" @click="next">
      <span aria-hidden="true" class="carousel-control-next-icon"></span>
    </a>
    
    <b-carousel-slide
      v-for="(list, idx) in carousel"
      :key=idx
      style="width: 100%; height: 100%; margin-right: 0%"
      background="purple"
    >
      <Slide
        id="slide"
        v-for="(movie, idx2) in list"
        :key=idx2
        :movieId="movie.movie_id"
        :listId="listId"
      />
    </b-carousel-slide>
  </b-carousel>
</template>





<script>
import Slide from '@/components/MovieList/Carousel/Slide'


export default {
  name: 'Carousel',
  components: {
    Slide,
  },
  props: {
    carousel: {
      type: Array
    },
    listId: {
      type: Number,
    }
  },
  methods: {
    prev() {
      this.$refs.myCarousel.prev()
    },
    next() {
      this.$refs.myCarousel.next()
    },
  }
}
</script>

<style>
  .carousel-inner {
    width: 100%;
    height: 100%;
  }
  .carousel-caption {
    background: black;
    position: relative !important;
    width: 100% !important;
    height: 100% !important;
    right: 0% !important;
    left: 0% !important;
    bottom: 0% !important;
    top: 0% !important;
    padding-top: 0% !important;
    padding-bottom: 0% !important;
  }
  #slide {
    position: relative;
    overflow: hidden;
    width: 19%;
    height: 100%;
    display: inline-block;
    /* top: 18%; */
  }
</style>