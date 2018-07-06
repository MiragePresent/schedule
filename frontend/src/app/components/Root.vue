<template>
<v-app light>
  <v-content>
    <v-container>
      <router-view></router-view>
    </v-container>
  </v-content>
  <v-footer app></v-footer>
</v-app>
</template>

<script>
  import { mapActions } from 'vuex';
  export default {
    name: 'root',
    methods: {
      ...mapActions('task', ['fetchTasks'])
    },
    created() {
      this.fetchTasks();
    },
  }
</script>

<style>
</style>
