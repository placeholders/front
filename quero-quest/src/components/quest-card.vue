<template>
  <vk-card>
    <div class="body">
      <h3 class="title">{{ title }}</h3>
      <h4 class="user">{{ user }}</h4>
      <p class="desc small-text">{{ desc }}</p>
      <div class="votes-up">
        <img src="@/assets/upvote.png" />
        {{ up }}
      </div>
      <div class="votes-down">
        <img src="@/assets/downvote.png" />
        {{ down }}
      </div>
    </div>
  </vk-card>
</template>


<script>
import axios from 'axios'

export default {
  name: "QuestCard",
  props:{
    user:String,
    title:String,
    up:Number,
    down:Number,
    desc:String,
    questId:Number,
  },
  methods: {
    voteup: function(){
      axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/issue/update/upvote',
        data:{
          login: window.sessionStorage.getItem("user"),
          issue_id: this.questId,
        }
      })
    },
    votedown: function(){
      axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/issue/update/downvote',
        data:{
          login: window.sessionStorage.getItem("user"),
          issue_id: this.questId,
        }
      })
    },
  },
}
</script>


<style scoped>
.body {
  display: grid;
  grid-template:
    "title title desc" 1fr
    "user  user  desc" 1fr
    "up    down  desc" 1fr
    / 1fr 1fr 2fr
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
