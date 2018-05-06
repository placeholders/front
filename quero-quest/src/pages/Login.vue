<template>
  <div id="login">
      <vk-notification
        status="danger"
        :messages.sync="messages"
        />
      <vk-card class="uk-width-1-3@m uk-position-absolute uk-transform-center" style="left:50%;top:50%">
          <vk-card-title slot="header">
                Login
          </vk-card-title>
          <form>
                <FormInput
                    input-id="txtLogin"
                    input-placeholder="my awesome nickname"
                    label-text="Username"
                    v-model="user"
                    />

                <FormInput
                    input-id="txtPassword"
                    input-type="password"
                    input-placeholder="*******"
                    label-text="Password"
                    v-model="pass"
                    />

                <div class="uk-margin" uk-margin>
                    <button
                        class="uk-button uk-button-primary"
                        @click="login()"
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
import axios from 'axios'
import FormInput from '@/components/form-input.vue'

export default {
    data(){return{
        messages: [],
        user: "",
        pass: "",
    }},
    methods: {
        navigateTo: function(to){
            window.router.push(to)
        },
        validate: function(){
            if ([this.user,this.pass].indexOf("") !== -1){
                this.messages.push("Fill all the fields")
                return false
            }
            return true
        },
        login: function(){
            if (!this.validate()){
                return
            }

            axios({
                method: 'post',
                url: 'http://127.0.0.1:5000/login',
                data: {
                    login: this.user,
                    password: this.pass,
                }
            }).then(response => {
                if(response.data.status !== 0){ 
                    this.messages.push( response.data.message )
                    return
                }

                window.sessionStorage.setItem("user", this.user)
                this.navigateTo("/")
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
#signup {
    margin-left: 1rem;
}
</style>
