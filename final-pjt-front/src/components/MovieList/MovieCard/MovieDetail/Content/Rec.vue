<template>
  <div>
    <div class="left" style="background-color: transparent">
      <br>
      <br>
      <br>
      <br>
      <br>
      <p class="title">이런 영화는 어때요?</p>
    </div>
    <div class="right" :style="`background: linear-gradient(215deg, transparent 10%, black), url('https://image.tmdb.org/t/p/w1280/${movie.backdrop_path}'); background-size: 100% auto !important; opacity:0.3;`">
    </div>
    <div class="reclist">
      <RecListItem 
        v-for="(item, idx) in recList"
        :key=idx
        :item="item"
      />
    </div>
  </div>
</template>

<script>
import RecListItem from '@/components/MovieList/MovieCard/MovieDetail/Content/RecListItem'
import axios from 'axios'

export default {
  name: 'Rec',
  components: {
    RecListItem,
  },
  data: function () {
    return {
      recList: []
    }
  },
  computed: {
    movie: function () {
      return this.$store.state.movie
    }
  },
  created: function () {
    axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/movie/${this.$store.state.movie.movie_id}/similar?api_key=f361f3c50ed76f4dd96355b1957b3f29&language=ko-KR&page=1`
    })
      .then(res => {
        this.recList = res.data.results.slice(0,3)
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style scoped>
  .title {
    color: white;
    font-size: 2.5rem;
  }
  .left {
    position: absolute;
    display: inline-block;
    right: 0%;
    width: 100%;
    height: 300px;
    z-index: 1;
    text-align: center;
  }
  .right {
    position: absolute;
    display: inline-block;
    left: 0%;
    width: 100%;
    height: 300px;
  }
  .reclist {
    position: relative;
    top: 300px;
    height: 420px;
  }
</style>