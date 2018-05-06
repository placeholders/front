<template>
<div id="quests" class="uk-width-2-3@m">
    <div v-if="quests.lenght <= 0">Nothing to see here.</div>
    <QuestCard
        v-for="q in quests"
        :key="q.quest_id"
        :user="q.user_creator"
        :title="q.title"
        :up="q.up_votes"
        :down="q.down_votes"
        :desc="q.description"
        @click="openQuest(q.quest_id)"
        />
</div>
</template>

<script>
import QuestCard from './quest-card.vue'
import axios from 'axios'

export default {
    data(){return{
        quests: [],
    }},
    name: "QuestContainer",
    components: {
        QuestCard,
    },
    methods:{
        openQuest: function(id){
            window.router.push(`/quest/${id}`)
        }
    },
    mounted: function (){
        axios({
            method: 'get',
            url: 'http://127.0.0.1:5000/quests'
        }).then(response => {
            this.quests = response.data.quests
        })
    }
}
</script>


<style scoped>
#quests {
    display: flex;
    align-items: stretch;
    flex-flow: column nowrap;

    margin: 0 auto;
}
#quests > * {
    margin-bottom: 2.5rem;
}
</style>
