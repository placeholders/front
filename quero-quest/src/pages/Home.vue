<template>
<div id="main">
	<NavTest/>
    <vk-card>
        <vk-card-title>wololo</vk-card-title>
    </vk-card>

    <vk-card>
        <vk-card-title>wololo</vk-card-title>
        <vk-label slot="badge" type="success">new</vk-label>
    </vk-card>
</div>
</template>

<script>
import NavTest from '@/components/nav-test.vue'

export default {
	components:{
		NavTest
	}
}
</script>
