import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/pages/Home'
import Login from '@/pages/Login'
import Signup from '@/pages/Signup'
import PostAQuest from '@/pages/Postaquest'

Vue.use(VueRouter)

window.router = new VueRouter({
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
        {
            path: '/signup',
            name: 'signup',
            component: Signup
        },
        {
            path: '/post',
            name: 'post',
            component: PostAQuest
        },
    ]
})

export default window.router