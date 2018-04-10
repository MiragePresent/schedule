import Vue from 'vue'

import store from './config/store'
import router from './config/router'
import { sync } from 'vuex-router-sync'

import Root from './components/Root'

sync(store, router)

const app = new Vue({
  router,
  store,
  ...Root
})

export {app, router, store}
