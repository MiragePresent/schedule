<template>
  <div class="">
    <v-layout row>
      <v-flex xs12 sm10 offset-sm1>
        <v-card>
          <v-toolbar color="light-blue" dark>
            <v-toolbar-side-icon></v-toolbar-side-icon>
            <v-toolbar-title>Tasks</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn icon @click="appendTask()">
              <v-icon>add_circle</v-icon>
            </v-btn>
          </v-toolbar>
          <v-list>
            <task-item avatar v-for="task in tasks" :task="task"></task-item>
         </v-list>
       </v-card>
     </v-flex>
   </v-layout>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex';
  import DateTime from 'vue-datetime';
  import uuid from 'uuid/v1';
  import TaskItem from './TaskItem.vue';
  export default {
    props: {
      filter: null,
    },
    computed: {
      ...mapGetters('task', ['tasks']),
    },
    components: {
      TaskItem,
    },
    methods: {
      ...mapActions('task', ['emptyTask', 'setEdit']),
      appendTask() {
        let id = uuid();
        this.setEdit(id);
        this.emptyTask({ id: id, status: 1 });
      },
    }
  };
</script>

<style lang="scss">
</style>
