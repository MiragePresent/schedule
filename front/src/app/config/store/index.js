import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from 'vuex/dist/logger'

import ajax from './modules/ajax'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    ajax
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
})
