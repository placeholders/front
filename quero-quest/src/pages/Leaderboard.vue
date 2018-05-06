
<template>
<div id="main">
    <header>
        <NavApp />
    </header>
    <main>
        <LeaderBoard />
    </main>
</div>

</template>

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

<script>
import LeaderBoard from '@/components/app-leaderboard.vue'

export default {
    components:{
        LeaderBoard,
    }
}
</script>