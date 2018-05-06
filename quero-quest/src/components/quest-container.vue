<template>
<div id="quests" class="uk-width-2-3@m">
<<<<<<< 65124646495cc8b02e4ea2c03b096b6b41e2fa89
        <QuestContent/>    

        <QuestContent/>
=======
    <QuestCard />
>>>>>>> Fixed positioning in card
</div>
</template>
<script type="text/javascript">
   import QuestContent from '@/components/quest-card.vue' 

<<<<<<< 65124646495cc8b02e4ea2c03b096b6b41e2fa89
    export default {
    components:{
        QuestContent,
    }
}
</script>
=======
<script>
import QuestCard from './quest-card.vue'

export default {
    name: "QuestContainer",
    components: {
        QuestCard,
    }
}
</script>


>>>>>>> Fixed positioning in card
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
