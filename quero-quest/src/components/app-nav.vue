<template>
  <vk-navbar>
    <vk-navbar-nav slot="left">
      <vk-navbar-logo>
        <img src="@/assets/artproquest.png" />
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
      <vk-navbar-nav-item>{{ user }}</vk-navbar-nav-item>
      <vk-button type="primary" @click="logout()">Logout</vk-button>
    </vk-navbar-nav>
  </vk-navbar>
</template>

<script>
export default {
  data(){return{
    user: window.sessionStorage.getItem("user"),
  }},
  methods:{
    logout: function(){
      window.sessionStorage.clear()
      this.navigateTo("/login")
    },
    navigateTo: function(to){
      window.router.push(to)
    }
  }
}
</script>

<style scoped>
.router-link-exact-active{
  color: #111
}
</style>
