<template>
  <vk-navbar>
    <vk-navbar-nav slot="left">
      <vk-navbar-logo>
        <router-link
          to="/">
          <img src="@/assets/artproquest.png" />
        </router-link>
      </vk-navbar-logo>

      <li><router-link
        to="/">
        Quests
      </router-link></li>
      <li><router-link
        to="/post">
        Post a Quest
      </router-link></li>
      <li><router-link
        to="/board">
        Leaderboard
      </router-link></li>
    </vk-navbar-nav>
    <vk-navbar-nav slot="right" class="uk-padding-small">
      <li>Hey, {{ user }}!</li>
      <vk-button type="primary" @click="logout()">Logout</vk-button>
    </vk-navbar-nav>
  </vk-navbar>
</template>

<script>
export default {
  data(){return{
    user: "",
  }},
  methods:{
    logout: function(){
      window.sessionStorage.clear()
      this.navigateTo("/login")
    },
    navigateTo: function(to){
      window.router.push(to)
    }
  },
  mounted:function(){
    this.user = window.sessionStorage.getItem("user")
  }
}
</script>

<style scoped>
.router-link-exact-active{
  color: #111
}
</style>
