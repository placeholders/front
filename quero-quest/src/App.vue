<template>
  <router-view></router-view>
</template>

<script>
export default {
  data(){return{
    user: {
      login: "",
    }
  }},
  watch:{
    user: function(){
      window.sessionStorage.setItem("user", JSON.stringify(this.user))
    }
  },
  mounted: function(){
    this.user = JSON.parse(window.sessionStorage.getItem("user"))

    if (this.user == null){
      window.router.push("/login")
    }
  }
}
</script>