import Vue from 'vue';
import Vuetify from 'vuetify';
import VueToast from 'vue-toast';
import axios from 'axios';

import store from './store';
import router from './config/router';
import { sync } from 'vuex-router-sync';
import Root from './components/Root';
import 'vuetify/dist/vuetify.min.css';
import 'vue-toast/dist/vue-toast.min.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

sync(store, router);

Vue.use(Vuetify);
Vue.use(VueToast);

const app = new Vue({
  router,
  store,
  ...Root
});

axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
axios.defaults.headers.common['Content-Type'] = 'application/json';

export {app, router, store};
