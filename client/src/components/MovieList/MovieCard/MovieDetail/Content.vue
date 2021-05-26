<template>
  <div>
    <div style="height:90%">
      <Basic/>
      <Detail :movie-id="movie.movie_id"/>
      <Rec/>
    </div>
    <div style="height:10%">
      <button v-if="isBasic" @click="onBasic">기본정보</button>
      <button v-if="isDetail" @click="onDetail">상세정보</button>
      <button v-if="isRec" @click="onRec">비슷한 영화</button>
    </div>
  </div>
</template>

<script>
import Basic from '@/components/MovieList/MovieCard/MovieDetail/Content/Basic' 
import Detail from '@/components/MovieList/MovieCard/MovieDetail/Content/Detail' 
import Rec from '@/components/MovieList/MovieCard/MovieDetail/Content/Rec' 

export default {
  name: 'Content',
  components: {
    Basic,
    Detail,
    Rec,
  },
  data: function () {
    return {
      movie: this.$store.state.movie,
      isBasic: true,
      isDetail: false,
      isRec: false,
    }
  },
  methods: {
    onBasic() {
      this.isBasic = true
      this.isDetail = false
      this.isRec = false
    },
    onDetail() {
      this.isBasic = false
      this.isDetail = true
      this.isRec = false
    },
    onRec() {
      this.isBasic = false
      this.isDetail = false
      this.isRec = true
    }
  }
}
</script>

<style>
  
</style>