<template>
<div id="main">
    <header>
        <NavTest />
    </header>
    <main>
        <QuestContainer />
    </main>
</div>
</template>

<script>
import QuestContainer from '@/components/quest-container.vue'
import NavTest from '@/components/nav-test.vue'

export default {
    components:{
        QuestContainer,
		NavTest,
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
