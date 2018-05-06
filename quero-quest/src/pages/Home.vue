<template>
<div id="main">
	<NavTest/>
    <QuestContainer />
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
