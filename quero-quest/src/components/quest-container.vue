<template>
<div id="quests" class="uk-width-2-3@m">
    <QuestCard />
</div>
</template>

<script>
import QuestCard from './quest-card.vue'

export default {
    name: "QuestContainer",
    components: {
        QuestCard,
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
