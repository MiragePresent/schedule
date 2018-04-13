<template>
  <div class="">
    <v-layout row>
      <v-flex xs12 sm10 offset-sm1>
        <v-card>
          <v-toolbar color="light-blue" dark>
            <v-toolbar-side-icon @click="filtered = !filtered">
              <v-icon v-if="filtered">low_priority</v-icon>
              <v-icon v-else>list</v-icon>
            </v-toolbar-side-icon>
            <v-toolbar-title>Tasks</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-chip
              color="pink"
              text-color="white"
              v-if="doneTasksCount > 0"
            >
              <v-avatar
                icon="true"
                class="helper-icon"
              >
                <v-icon>check_circle</v-icon>
              </v-avatar>
              {{ doneTasksMessage }}
            </v-chip>
            <v-btn icon @click="appendTask()">
              <v-icon>add_circle</v-icon>
            </v-btn>
          </v-toolbar>
          <v-list
            :style="listStyle"
            class="scroll-y"
          >
            <task-item avatar v-for="task in tasksList" :task="task"></task-item>
            <task-list-empty v-if="!tasksList.length"/>
         </v-list>
       </v-card>
     </v-flex>
   </v-layout>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex';
  import uuid from 'uuid/v1';
  import TaskItem from './TaskItem.vue';
  import TaskListEmpty from './TaskListEmpty.vue';
  export default {
    computed: {
      ...mapGetters('task', ['tasks', 'editTask']),
      ...mapGetters('client', ['height']),
      tasksList() {
        return this.filtered ? this.tasks.filter(task => !task.status) : this.tasks;
      },
      listStyle() {
        return {
          maxHeight: (this.height - 130) + 'px',
        };
      },
      doneTasksCount() {
        return this.tasks.filter(task => task.status == 1).length;
      },
      doneTasksMessage() {
        return `${this.doneTasksCount} ${(this.doneTasksCount == 1 ? 'task is' : 'tasks are')} done`;
      }
    },
    components: {
      TaskItem,
      TaskListEmpty,
    },
    data() {
      return {
        filtered: true,
      };
    },
    methods: {
      ...mapActions('task', ['emptyTask', 'setEdit']),
      appendTask() {
        if (!this.editTask) {
          let id = uuid();
          this.setEdit(id);
          this.emptyTask({ id: id, status: 0 });
        } else {
          this.$toastr('info', 'Please done editing of another task');
        }
      },
    }
  };
</script>

<style lang="scss">
  .helper-icon {
    padding-top: 7px;
  }
  .toast-message {
    font-family: 'Roboto', sans-serif !important;
  }
</style>
