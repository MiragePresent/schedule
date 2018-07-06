import Vue from 'vue';
import Vuex from 'vuex';
import createLogger from 'vuex/dist/logger';

import task from './modules/task';
import client from './modules/client';

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    task,
    client,
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
})
