<template>
<div id="main">
    <header>
        <NavApp />
    </header>
    <main>
        <QuestContainer />
    </main>
</div>
</template>

<script>
import QuestContainer from '@/components/quest-container.vue'
import NavApp from '@/components/app-nav.vue'


export default {
    components:{
        QuestContainer,
		NavApp,
    }
}
</script>

<style scoped>
#main {
    display: grid;
    grid-template:
        "header"
        "main";
}
#main header{
    grid-area: header;

    margin-bottom: 2.5rem;
}
#main main{
    grid-area: main;
}
</style>
