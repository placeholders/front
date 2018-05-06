<template>
  <div id="login">
      <vk-card class="uk-width-1-5@m uk-position-absolute uk-transform-center" style="left:50%;top:50%">
          <vk-card-title slot="header">
                Registro
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
                <FormInput
                    input-id="txtPassword"
                    input-type="password"
                    input-placeholder="*******"
                    label-text="Reenter Password"
                    />

                <div class="uk-margin" uk-margin>
                    <button
                        class="uk-button uk-button-primary"
                        type="button">
                        Register
                    </button>
                </div>
                <div class="uk-margin" uk-margin>
                    <button
                        class="uk-button uk-button-primary"
                        type="button">
                        clean
                    </button>
                </div>
          </form>
      </vk-card>
  </div>
</template>

<script>
import FormInput from '@/components/form-input.vue'

export default {
    components: {
        FormInput
    }
}
</script>

<style>
#login {
  padding: 10px;
}
</style>
