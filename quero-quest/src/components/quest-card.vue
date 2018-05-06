<template>
  <vk-card>
    <div class="body">
      <div class="title">
        <h3>placeholder problem title</h3>
      </div>
      <div class="vote">
      <img src="@/assets/upvote.png" @click="upvote"/>
      <div class="votes" id="voted">
      <img src="@/assets/questing.png"/>
      </div>
      <div class="vote" id="votet">
      <img src="@/assets/downvote.png" @click="downvote"/>
      <span class="label label-primary">{{ votes }}</span>
      </div>
      <div class="desc small-text">
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit eos neque non facilis tempora reprehenderit harum animi sint necessitatibus minima? Cum tenetur veniam harum porro maiores exercitationem accusantium, praesentium magnam commodi, cupiditate ducimus asperiores adipisci. Aliquid, repellat repudiandae voluptatem eos dolore cumque quas nostrum, perferendis doloremque, aliquam accusantium placeat eaque?</p>
      </div>	
    </div>
  </div>
  </vk-card>
</template>


<script>
export default {
  name: "QuestCard",
}

Vue.component('post', {
  template: "#post-template",
  props: ['post'],
  data: function () {
    return {
      upvoted: false,
      downvoted: false
    };
  },
  methods: {
    upvote: function () {
      this.upvoted = !this.upvoted;
      this.downvoted = false;
    },
    downvote: function () {
      this.downvoted = !this.downvoted;
      this.upvoted = false;
    }
  },
  computed: {
    votesu: function () {
      if (this.upvoted) {
        return this.post.votes + 1;
      } else if (this.downvoted) {
        return this.post.votes - 1;
      } else {
        return this.post.votes;
      }
    }
  }
});
</script>


<style scoped>
.body {
  display: grid;
  grid-template:
    "title desc" 1fr
    "votes desc" 1fr
    / 1fr 2fr
    

}
.body .title {
  grid-area: title;

}
.body .title > * { 
	font-size: 1.3rem;
  font-weight: bold;
}
.small-text {
  font-size: 0.95rem;
}
.body .votes {
  grid-area: votes;
}
.body .votes2 {
  grid-area: votes2;
}
.body .votes3 {
  grid-area: votes3;
}
.body .desc {
  grid-area: desc;
}
#voted{
  padding-left: 10%;
}
#votet{
  padding-left: 10%;
}
</style>
