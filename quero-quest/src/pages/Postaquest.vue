<template>
  <div id="login">
      <vk-card class="uk-width-1-5@m uk-position-absolute uk-transform-center" style="left:50%;top:50%">
          <vk-card-title slot="header">
                Post a Quest
          </vk-card-title>
          <form>d
                <FormInput
                    input-id="txtquest"
                    input-placeholder="Quest"
                    label-text="Quest Title"
                    />

                <FormInput
                    input-id="txtquestresume"
                    input-placeholder="Here you write your quest resume"
                    label-text="Quest small resume"
                    />

                <FormInput
                    input-id="txtquestr"
                    input-placeholder="Here you write your quest"
                    label-text="Quest"
                    />

                <div class="uk-margin" uk-margin>
                    <button
                        class="uk-button uk-button-primary"
                        type="button">
                        Submit it
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
