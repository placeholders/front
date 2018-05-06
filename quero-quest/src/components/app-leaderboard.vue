<template>
  <table class="uk-table uk-table-striped">
    <thead>
        <tr>
            <th>Name</th>
            <th>Score</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="line in lines" :key="line.name">
            <td>{{ line.name }}</td>
            <td>{{ line.score }}</td>
        </tr>
    </tbody>
</table>
</template>

<script>
import axios from 'axios'

export default {
  data(){return{
      lines: [],
  }},
  mounted: function(){
      axios({
          method: 'get',
          url: 'http://127.0.0.1:5000/users/scores',
      }).then(response =>{
          this.lines = response.data.users
      })
  },
}
</script>

<style scoped>
.uk-table{
    margin: 2rem;
}
</style>
