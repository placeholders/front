<template>
<div>
  <QuestCard
    :user="quest.creator"
    :title="quest.title"
    :up="quest.up_votes"
    :down="quest.down_votes"
    :desc="quest.description"
    />
  <FormInput
    input-id="txtanswer"
    input-placeholder="Here you write your answer"
    label-text="Answer"
    v-model="full"
    />
</div>
</template>


<script>
import axios from 'axios'
import QuestCard from '@/components/quest-card.vue'

export default {
  props:{
    quest: Object,
  },
  components:{
    QuestCard,
  },
  mounted:function(){
      axios({
          method: 'post',
          url: 'http://127.0.0.1:5000/quest/get',
          data:{
              id: this.$route.params.id,
          }
      }).then(response => {
          this.quest = response.data
      })
  }
}
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
  padding-left: 32.5%;
}
#votet{
  padding-left: 65%;
}
</style>