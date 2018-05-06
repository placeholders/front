<template>
<div>
    <AppNav />

    <div id="container" class="uk-width-2-3@m">
        <QuestCard
            :key="$route.params.id"
            :user="quest.creator"
            :title="quest.title"
            :up="quest.up_votes"
            :down="quest.down_votes"
            :desc="quest.description"
            />

        <div class="desc">
            <label>
                Description:
                <p>{{ quest.description }}</p>
            </label>
        </div>

        <FormInput
            input-id="txtAnswer"
            input-placeholder="Here you write your answer"
            label-text="Answer"
            v-model="full"
            />

        <button class="uk-button uk-button-primary">Submit</button>    
    </div>
</div>
</template>


<script>
import axios from 'axios'
import AppNav from '@/components/app-nav.vue'
import QuestCard from '@/components/quest-card.vue'
import FormInput from '@/components/form-input.vue'

export default {
  props:{
    quest: Object,
  },
  components:{
    QuestCard,
    FormInput,
    AppNav,
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
#container {
    display: flex;
    align-items: stretch;
    flex-flow: column nowrap;

    margin: 2.5rem auto 0;
}
.desc {
    font-size: 2rem;
}
</style>