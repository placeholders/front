<template>
  <vk-card>
    <div class="body">
      <label>
        Title:
        <h3 class="title" @click="openIt($vnode.key)">{{ title }}</h3>
      </label>

      <label>
        User:
        <h4 class="user">{{ user }}</h4>
      </label>

      <div class="votes-up uk-button" @click="voteup()">
        <img src="@/assets/upvote.png" />
        {{ realUp }}
      </div>
      <div class="votes-down uk-button" @click="votedown()">
        <img src="@/assets/downvote.png" />
        {{ realDown }}
      </div>

    </div>
  </vk-card>
</template>


<script>
import axios from 'axios'

export default {
  name: "QuestCard",
  data(){return{
    realUp: this.up,
    realDown: this.down,
  }},
  props:{
    user:String,
    title:String,
    up:Number,
    down:Number,
    desc:String,
    questId:Number,
  },
  methods: {
    openIt:function(id){
      console.log("card clicked: ", id)
      this.$router.push("/quest/"+id)
    },
    voteup: function(){
      axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/issue/update/upvote',
        data:{
          login: window.sessionStorage.getItem("user"),
          issue_id: this.$vnode.key,
        }
      }).then(response => {
        this.realDown = response.data.down_votes
        this.realUp = response.data.up_votes
      })
    },
    votedown: function(){
      axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/issue/update/downvote',
        data:{
          login: window.sessionStorage.getItem("user"),
          issue_id: this.$vnode.key,
        }
      }).then(response => {
        this.realDown = response.data.down_votes
        this.realUp = response.data.up_votes
      })
    },
  },
}
</script>


<style scoped>
.body {
  display: grid;
  grid-template:
    "title up" 1fr
    "user  down" 1fr
    / 2fr 1fr
}
.body .title {
  grid-area: title;

	font-size: 1.3rem;
  font-weight: bold;
}
.small-text {
  font-size: 0.95rem;
}
.body .votes-up {
  grid-area: up;
}
.body .votes-down {
  grid-area: down;
}
.body .desc {
  grid-area: desc;
}
.body .user {
  grid-area: user;
}
</style>
