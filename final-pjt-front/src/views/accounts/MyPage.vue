<template>
  <div>
    <div id="app">
        <h1>선호하는 영화 장르</h1>
        <wordcloud
        :data="defaultWords"
        nameKey="name"
        valueKey="value"
        :color="myColors"
        :showTooltip="true"
        :wordClick="wordClickHandler">
        </wordcloud>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import wordcloud from 'vue-wordcloud'

export default {
  name: 'MyPage',
  components: {
    wordcloud
  },
  methods: {
    wordClickHandler(name, value, vm) {
      console.log('wordClickHandler', name, value, vm);
    }
  },
  data() {
    return {
      username: this.$store.state.username,
      setToken: this.$store.state.setToken(),
      myColors: ['#6200B3', '#9B21FF', '#C175FF', '#DFB9FF'],
      defaultWords: [{
          "name": "액션",
          "num": "28",
          "value": 0
        },
        {
          "name": "모험",
          "num": "12",
          "value": 0
        },
        {
          "name": "애니메이션",
          "num": "16",
          "value": 0
        },
        {
          "name": "코미디",
          "num": "35",
          "value": 0
        },
        {
          "name": "범죄",
          "num": "80",
          "value": 0
        },
        {
          "name": "다큐멘터리",
          "num": "99",
          "value": 0
        },
        {
          "name": "드라마",
          "num": "18",
          "value": 0
        },
        {
          "name": "가족",
          "num": "10751",
          "value": 0
        },
        {
          "name": "판타지",
          "num": "14",
          "value": 0
        },
        {
          "name": "역사",
          "num": "36",
          "value": 0
        },
        {
          "name": "공포",
          "num": "27",
          "value": 0
        },
        {
          "name": "음악",
          "num": "10402",
          "value": 0
        },
        {
          "name": "미스터리",
          "num": "9648",
          "value": 0
        },
        {
          "name": "로맨스",
          "num": "10749",
          "value": 0
        },
        {
          "name": "SF",
          "num": "878",
          "value": 0
        },
        {
          "name": "TV 영화",
          "num": "10770",
          "value": 0
        },
        {
          "name": "스릴러",
          "num": "53",
          "value": 0
        },
        {
          "name": "전쟁",
          "num": "10752",
          "value": 0
        },
        {
          "name": "서부",
          "num": "37",
          "value": 0
        },
      ]
    }
  },
  created: function () {
    const user = {
        username: this.username,
    }
    const defaultWords = this.defaultWords
    axios ({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/',
        data: user,
        headers: this.setToken,
      })
        .then(res => {
          // console.log(res)
          const movie = res.data.movie
          for (var like_movie = 0; like_movie < movie.length; like_movie++){
            const genre = res.data.movie[like_movie].genre.split(',')
            for (var genre_cnt = 0; genre_cnt < genre.length; genre_cnt++){
              for (var word_cnt = 0; word_cnt < defaultWords.length; word_cnt++){
                if (genre[genre_cnt] === defaultWords[word_cnt].num){
                  this.defaultWords[word_cnt].value++;
                  break;
                }
              }
            }
          }
          this.defaultWords = this.defaultWords.filter(defaultWord => defaultWord.value > 0)
            this.defaultWords.sort()
            this.$store.dispatch('createFavGenre', this.defaultWords.slice(0,3))
        })
        .catch(err => {
          console.log(err)
        })

  }
}
</script>

<style>
#app {
  font-family: SEBANG_Gothic_Bold;
  color: white;
}
</style>