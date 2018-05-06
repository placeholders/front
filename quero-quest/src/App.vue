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
      window.sessionStorage.setItem("user", this.user)
    }
  },
  mounted: function(){
    this.user = window.sessionStorage.getItem("user")

    if (this.user == null){
      window.router.push("/login")
    }
  }
}
</script>