<template>
<div id="quests" class="uk-width-2-3@m">
        <QuestContent/>    

        <QuestContent/>
</div>
</template>
<script type="text/javascript">
   import QuestContent from '@/components/quest-card.vue' 

    export default {
    components:{
        QuestContent,
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
