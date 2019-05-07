<template>
  <v-layout row>
  <v-flex xs12 sm8 offset-sm2>
    <v-card>
      <v-toolbar color="blue" dark>
        <v-toolbar-side-icon
          :title="filterTitle"
          @click="filtered = !filtered"
        >
          <v-icon v-if="filtered">list</v-icon>
          <v-icon v-else>low_priority</v-icon>
        </v-toolbar-side-icon>
        <v-toolbar-title>TODO</v-toolbar-title>
        <task-list-navigation/>
        <v-spacer></v-spacer>
        <v-chip
          color="pink"
          text-color="white"
          v-if="numberOfDoneTasks > 0"
        >
          <v-avatar class="pink darken-4">{{ numberOfDoneTasks }}</v-avatar>
          {{ ( numberOfDoneTasks > 1 ? "tasks are " : "task is " ) }} done
        </v-chip>
        <v-btn
          icon
          title="Add a task"
          :disabled="!!editTask"
          @click="appendTask()"
        >
          <v-icon>add_circle</v-icon>
        </v-btn>
      </v-toolbar>
      <v-list>
        <task-item
          v-for="task in taskList"
          :task="task"
        />
        <task-list-empty v-if="!taskList.length"/>
      </v-list>
    </v-card>
  </v-flex>
</v-layout>
</template>

<script>
import {
  mapGetters,
  mapActions,
} from 'vuex';
import uuidv1 from 'uuid/v1';
import TaskItem from './TaskItem';
import TaskListEmpty from './TaskListEmpty';
import TaskListNavigation from './TaskListNavigation';
export default {
  components: {
    TaskItem,
    TaskListEmpty,
    TaskListNavigation,
  },
  computed: {
    ...mapGetters('task', ['tasks', 'editTask', 'selectedDate']),
    taskList() {
      return this.filtered ? this.tasks.filter(task => !task.status) : this.tasks;
    },
    numberOfDoneTasks() {
      return this.tasks.filter(task => !!task.status).length;
    },
    filterTitle() {
      return this.filtered ? 'Show all tasks' : 'Hide done tasks';
    },
  },
  data() {
    return {
      filtered: true,
    };
  },
  methods: {
    ...mapActions('task', [ 'emptyTask', 'setEdit']),
    appendTask() {
      let uuid = uuidv1();
      this.emptyTask({ id: uuid, date: this.selectedDate });
      this.setEdit(uuid);
    }
  }
}
</script>

<style lang="css">
</style>
