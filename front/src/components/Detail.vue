<template>
  <v-card class="mx-auto" min-height="400">
    <v-card-text v-if="result">
      <div>{{ result.word }}</div>
      <p class="display-1 text--primary">{{ result.result }}</p>
      <p>{{ result.translate }}</p>
      <div class="text--primary">{{ result.additional }}</div>
    </v-card-text>
  </v-card>
</template>
<script>
export default {
  name: "Detail",

  computed: {
    result() {
      return this.$store.state.result;
    }
  }
};
</script>
<style lang="stylus" scoped></style>