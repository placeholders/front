<template>
  <router-view></router-view>
</template>

<script>
export default {
  mounted: function(){
    let user = JSON.parse(window.sessionStorage.getItem("user"))

    if (user == null){
      window.router.push("/login")
    }
  }
}
</script>