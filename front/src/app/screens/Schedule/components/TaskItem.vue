<template>
  <v-list-tile avatar :key="task.title">
    <v-list-tile-action>
      <v-icon
        v-if="task.status == 0"
        color="pink"
        @click="setStatus('1')"
      >
        check_box_outline_blank
      </v-icon>
      <v-icon
        v-else
        color="pink"
        @click="setStatus('0')"
      >
        check_box
      </v-icon>
    </v-list-tile-action>
    <v-list-tile-content>
      <v-list-tile-title
        v-if="!showInput"
        v-text="task.title"
        :class="[titleClass]"
        @click="toggleEditMode()"
      />
      <v-form
        v-model="valid"
        ref="form"
        class="input_form"
        @submit="save"
      >
        <v-text-field
            single-line
            name="title"
            label="What do you need to do?"
            v-model="title"
            v-if="showInput"
            :rules="titleRules"
            @keyup.esc="cancelEdit()"
        />
      </v-form>
    </v-list-tile-content>
    <v-list-tile-action>
      <v-btn
        icon
        ripple
        @click="selfDelete"
      >
        <v-icon color="red lighten-1">close</v-icon>
      </v-btn>
    </v-list-tile-action>
  </v-list-tile>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  props: {
    task: {},
  },
  data() {
    return {
      valid: false,
      title: this.task.title,
      titleRules: [
        (title) => {
          if (typeof title === 'string') {
            return title.length > 2 || 'Title muts has more than 2 characters';
          }
          return true;
        },
        (title) => {
          if (typeof title === 'string') {
            return title.length <= 100 || 'Title must be less than 100 characters';
          }
          return true;
        }
      ],
    };
  },
  computed: {
    ...mapGetters('task', ['editTask']),
    showInput() {
      return this.editTask === this.task.id;
    },
    titleClass() {
      return this.task.status == 1 ? 'editable' : 'non-editable';
    },
  },
  methods: {
    ...mapActions('task', ['updateTask', 'createTask', 'setEdit', 'deleteTask']),
    toggleEditMode() {
      if (this.task.status == 0) {
        if (this.showInput) {
          this.setEdit(null);
        } else {
          this.setEdit(this.task.id);
        }
      }
      return this.editMode;
    },
    save(event) {
      event.preventDefault();
      if (this.valid) {
        this.editMode = false;
        if (parseInt(this.task.id) == this.task.id) {
          this.updateTask({ task_id: this.task.id, data: { title: this.title } });
          this.setEdit(null);
        } else {
          this.createTask({ uuid: this.task.id, title: this.title });
          this.setEdit(null);
        }
      }
    },
    selfDelete() {
      this.deleteTask(this.task.id);
    },
    setStatus(status) {
      this.updateTask({ task_id: this.task.id, data: { status: status }});
    },
    cancelEdit() {
      this.title = this.task.title;
      this.editMode = false;
    }
  },
}
</script>
<style>
  .input_form{
    width: 100%;
  }
  .editable{
    cursor: pointer;
  },
  .non-editable{
    cursor: default;
  },
  li {
     list-style-type: none;
  }
</style>
