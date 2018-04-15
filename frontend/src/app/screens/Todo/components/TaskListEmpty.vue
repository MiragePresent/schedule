<template>
  <v-list-tile>
    <v-list-tile-content>
      <v-list-tile-title
        v-text="message"
        class="text-md-center"
      />
    </v-list-tile-content>
  </v-list-tile>
</template>

<script>
import {
  mapGetters,
  mapActions,
} from 'vuex';

export default {
  computed: {
    ...mapGetters('task', [ 'tasks' ]),
    message() {
      if (this.tasks.length > 1) {
        return 'Good job! All your tasks have been done';
      }
      return 'You have no tasks yet';
    }
  }
}
</script>

<style lang="css">
</style>
