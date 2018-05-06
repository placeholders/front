import Vue from 'vue/dist/vue.js'
import App from './App.vue'
import VueRouter from 'vue-router'

import router from './router'

import Vuikit from 'vuikit'
import '@vuikit/theme'

Vue.use(Vuikit)
Vue.use(VueRouter)

Vue.config.productionTip = false

window.app = new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})