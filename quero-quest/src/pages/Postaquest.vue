<template>
  <div id="post">
      <header>
          <AppNav />
      </header>
      <vk-card class="uk-width-1-5@m uk-position-absolute uk-transform-center" style="left:50%;top:50%">
          <vk-card-title slot="header">
                Post a Quest
          </vk-card-title>
          <form>
                <FormInput
                    input-id="txtquest"
                    input-placeholder="Quest"
                    label-text="Quest Title"
                    v-model="title"
                    />

                <FormInput
                    input-id="txtquestr"
                    input-placeholder="Here you write your quest"
                    label-text="Quest"
                    v-model="full"
                    />

                <div class="uk-margin" uk-margin>
                    <button
                        @click="postIt()"
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
import AppNav from '@/components/app-nav.vue'

export default {
    data(){return{
        messages: [],

        title: "",
        full: "",
    }},
    methods: {
        postIt: function(){
            axiox({
                method: 'post',
                url: 'http://127.0.0.1:5000/issue/add',
                data: {
                    login: window.app.user.login,
                    title: this.title,
                    description: this.full,
                },
            }).then(response => {
                this.messages.push(response.data.message)
            })
        },
    },
    components: {
        AppNav,
        FormInput
    }
}
</script>

<style>
#login {
  padding: 10px;
}
</style>
