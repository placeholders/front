import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/pages/Home'
import Login from '@/pages/Login'

Vue.use(VueRouter)

export default new VueRouter({
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/login',
            name: 'login',
            component: Login
        },
    ]
})