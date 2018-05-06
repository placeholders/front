<template>
  <vk-navbar>
    <vk-navbar-nav slot="left">
      <vk-navbar-logo>
        <img src="@/assets/artproquest.png" />
      </vk-navbar-logo>

      <vk-navbar-nav-item
        title="Profile"
        />
      <vk-navbar-nav-item
        title="Quests"
        />
      <vk-navbar-nav-item
        title="Post a Quest"
        />
      <vk-navbar-nav-item
        title="Leaderboard"
        />
    </vk-navbar-nav>
    <vk-navbar-nav slot="right" class="uk-padding-small">
      <vk-button type="primary">Login</vk-button>
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

