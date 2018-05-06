<template>
  <div id="login">
      <vk-card class="uk-width-1-5@m uk-position-absolute uk-transform-center" style="left:50%;top:50%">
          <vk-card-title slot="header">
                Login
          </vk-card-title>
          <form>
                <FormInput
                    input-id="txtLogin"
                    input-placeholder="my awesome nickname"
                    label-text="Username"
                    />

                <FormInput
                    input-id="txtPassword"
                    input-type="password"
                    input-placeholder="*******"
                    label-text="Password"
                    />

                <div class="uk-margin" uk-margin>
                    <button
                        class="uk-button uk-button-primary"
                        type="button">
                        Login
                    </button>

                    <button
                        id="signup"
                        @click="navigateTo('signup')"
                        class="uk-button"
                        type="button">
                        Sign up
                    </button>
                </div>
          </form>
      </vk-card>
  </div>
</template>

<script>
import FormInput from '@/components/form-input.vue'

export default {
    methods: {
        navigateTo: function(to){
            window.router.push(to)
        },
    },
    components: {
        FormInput
    }
}
</script>

<style>
#login {
    padding: 10px;
}
#signup {
    margin-left: 1rem;
}
</style>
