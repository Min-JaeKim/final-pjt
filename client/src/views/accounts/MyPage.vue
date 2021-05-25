<template>
  <div>
    <h1 class="title">MyPage</h1>
    <h2>{{ this.username }}</h2>
  </div>
</template>


<script>
import axios from 'axios'
// headers에서 setToken으로 보내줘야함
export default {
  name: 'MyPage',
  data: function () {
    return {
      username: this.$store.state.username,
      setToken: this.$store.state.setToken(),
      
      genres: {
        '28': '액션',
        '12': '모험',
        '16': '애니메이션',
        '35': '코미디',
        '80': '범죄',
        '99': '다큐멘터리',
        '18': '드라마',
        '10751': '가족',
        '14': '판타지',
        '36': '역사',
        '27': '공포',
        '10402': '음악',
        '9648': '미스터리',
        '10749': '로맨스',
        '878': 'SF',
        '10770': 'TV 영화',
        '53': '스릴러',
        '10752': '전쟁',
        '37': '서부',
      }
    }
  },
  created: function () {
    const user = {
        username: this.username,
    }
    axios ({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/',
        data: user,
        headers: this.setToken,
      })
        .then(res => {
          console.log(res.data.movie[0].title)
        })
        .catch(err => {
          // console.log('hi')
          console.log(err)
        })
  }
}
</script>

<style>

</style>