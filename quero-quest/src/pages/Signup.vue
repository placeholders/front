<template>
  <div id="login">
      <vk-notification
        status="danger"
        :messages.sync="messages"
        />
      <vk-card class="uk-width-1-5@m uk-position-absolute uk-transform-center" style="left:50%;top:50%">
          <vk-card-title slot="header">
                Sign up
          </vk-card-title>
          <form>
                <FormInput
                    input-id="txtLogin"
                    input-placeholder="my awesome nickname"
                    label-text="Username"
                    v-model="username"
                    />

                <FormInput
                    input-id="txtLogin"
                    input-placeholder="my awesome fullname"
                    label-text="Your name:"
                    v-model="fullname"
                    />

                <FormInput
                    input-id="txtPassword"
                    input-type="password"
                    input-placeholder="*******"
                    label-text="Password"
                    v-model="password"
                    />

                <FormInput
                    input-id="txtConfPassword"
                    input-type="password"
                    input-placeholder="*******"
                    label-text="Confirm your password"
                    v-model="confpass"
                    />

                <div class="uk-margin" uk-margin>
                    <button
                        @click="signup()"
                        class="uk-button uk-button-primary"
                        type="button">
                        sign up
                    </button>
                </div>
          </form>
      </vk-card>
  </div>
</template>

<script>
import axios from 'axios'
import FormInput from '@/components/form-input.vue'

export default {
    data() {return{
        fullname: "",
        username: "",
        password: "",
        confpass: "",

        messages: [],
    }},
    methods: {
        validate: function(){
            if ([this.fullname,this.username,this.password,this.confpass].indexOf("") != -1){
                this.messages.push("Fill all fields")
                return false
            }
            return true
        },
        signup: function(){
            if (!this.validate()){
                return;
            }

            axios({
                method: 'post',
                url: 'http://127.0.0.1:5000/user/register',
                data: {
                    name: this.fullname,
                    login: this.username,
                    password: this.password,
                    confirmed_password: this.confpass,
                },
            })
            .then(response => {
                if (response.data !== "success"){
                    this.messages.push(response.data)
                    return
                }

                window.router.push("/login")
            })
        }
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
</style>
