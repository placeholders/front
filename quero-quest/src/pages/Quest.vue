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

        <FormInput
            input-id="txtAnswer"
            input-placeholder="Here you write your answer"
            label-text="Answer"
            v-model="solution"
            />

        <button
            class="uk-button uk-button-primary"
            @click="submit()">Submit</button>
    </div>
</div>
</template>


<script>
import axios from 'axios'
import AppNav from '@/components/app-nav.vue'
import QuestCard from '@/components/quest-card.vue'
import FormInput from '@/components/form-input.vue'
import questCardVue from '../components/quest-card.vue';

export default {
    data(){return{
        solution: "",
        quest: {},
    }},
    components:{
        QuestCard,
        FormInput,
        AppNav,
    },
    methods: {
      submit: function(){
          axios({
              method: 'post',
              url: 'http://127.0.0.1:5000/solution/add',
              data: {
                  login: window.sessionStorage.getItem("user"),
                  issue_id: this.$vnode.key,
                  desc: this.solution,
              }
          })
      }
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
    font-size: 1.25rem;
}
.desc p {
    color: #333;
}
</style>