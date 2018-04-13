<template>
  <v-list-tile avatar>
    <v-list-tile-content>
      <v-list-tile-title
        v-text="message"
        class="text-md-center"
      />
    </v-list-tile-content>
  </v-list-tile>
</template>
<script>
export default {
  data() {
    return {
      message: 'You have no tasks',
    };
  },
}
</script>
<style>
</style>
