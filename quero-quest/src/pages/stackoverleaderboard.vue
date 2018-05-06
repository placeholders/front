<template>
<div>
    <template v-for="item in list">
    </template>
</div>
</template>

<script>
export default {
    data(){return{
        list: [],
    }},
    mounted: function(){
        axios({

        }).then(response => {

        })
    }
}
</script>
