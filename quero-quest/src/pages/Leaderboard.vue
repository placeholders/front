
<template>
<div id="main">
    <header>
        <AppNav />
    </header>
    <main>
        <LeaderBoard />
    </main>
</div>

</template>

<script>
import AppNav from '@/components/app-nav.vue'
import LeaderBoard from '@/components/app-leaderboard.vue'

export default {
    components:{
        AppNav,
        LeaderBoard,
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