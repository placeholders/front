<template>
  <vk-navbar>
    <vk-navbar-nav slot="left">
      <vk-navbar-logo>
        <img src="@/assets/artproquest.png" />
      </vk-navbar-logo>

      <vk-navbar-nav-item
        title="Profile"
        />
      <li><router-link
        to="/">
        Quests
      </router-link></li>
      <li><router-link
        to="/post">
        Post a Quest
      </router-link></li>
      <vk-navbar-nav-item
        title="Leaderboard"
        />
    </vk-navbar-nav>
    <vk-navbar-nav slot="right" class="uk-padding-small">
      <vk-button type="primary">Logout</vk-button>
    </vk-navbar-nav>
  </vk-navbar>
</template>

<script>
export default {
  methods:{
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
