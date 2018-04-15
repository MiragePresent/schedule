<template>
  <v-list-tile>
    <v-list-tile-action class="pointer">
      <v-icon
        v-if="!! task.status"
        color="green"
        @click="setStatus(0)"
      >
        check_box
      </v-icon>
      <v-icon
        v-else
        color="grey"
        @click="setStatus(1)"
      >
        check_box_outline_blank
      </v-icon>
    </v-list-tile-action>
    <v-list-tile-content>
      <v-form
        v-if="showForm"
        v-model="valid"
        class="full-width"
        @submit="save"
      >
        <v-text-field
          label="What do you need to do?"
          v-model="title"
          :rules="titleRules"
          required
          single-line
          @keyup.esc="cancel()"
        ></v-text-field>
      </v-form>
      <v-list-tile-title
        v-else
        v-text="task.title"
        @click="openForm()"
      />
    </v-list-tile-content>
  </v-list-tile>
</template>

<script>
import {
  mapGetters,
  mapActions
} from 'vuex';
export default {
  props: {
    task: {}
  },
  computed: {
    ...mapGetters('task', [ 'editTask' ]),
    showForm() {
      return this.editTask === this.task.id;
    },
  },
  data() {
    return {
      valid: false,
      title: this.task.title,
      titleRules: [
        (title) => {
          if (typeof title === 'string') {
            return title.length > 2 || 'Title must contain at least 2 characters'
          }
          return 'Title is required';
        },
        title => {
          if (typeof title === 'string') {
            return title.length <= 100 || 'Title must be less than 10 characters'
          }
          return 'Title is required';
        },
      ],
    }
  },
  methods: {
    ...mapActions('task', ['createTask', 'updateTask', 'setEdit']),
    setStatus(status) {
      this.updateTask({task_id: this.task.id, data: { status }});
    },
    openForm() {
      if (!this.editTask) {
        this.setEdit(this.task.id);
      } else {
        // Show nofication
      }
    },
    save(event) {
      // Don't send form
      event.preventDefault();
      // Data for updating
      let data = { title: this.title };
      // if task is already save in DB it has numeric ID
      if (parseInt(this.task.id) == this.task.id) {
        this.updateTask({ task_id: this.task.id, data });
      // Else it's only stored in state task with uuid instead of real ID
      } else {
        this.createTask({ uuid: this.task.id, data });
      }
      // Close form
      this.setEdit(null);
    },
    cancel() {
      this.title = this.task.title;
      this.setEdit(null);
    },
  }

}
</script>

<style lang="css">
</style>
