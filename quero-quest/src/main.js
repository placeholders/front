import Vue from 'vue'
import App from './App.vue'
import Vuikit from 'vuikit'

import '@vuikit/theme'

Vue.config.productionTip = false

Vue.use(Vuikit)

new Vue({
  render: h => h(App)
}).$mount('#app')
