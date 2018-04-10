import Vue from 'vue'
import VueRouter from 'vue-router'

import routes from './routes'

const debug = process.env.NODE_ENV !== 'production'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: debug ? 'hash' : 'history',
  routes
})

export default router
