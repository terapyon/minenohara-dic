<template>
  <v-row>
    <v-col cols="3">
      <List />
    </v-col>
    <v-col cols="9">
      <Detail />
    </v-col>
  </v-row>
</template>
<script>
import List from "./List";
import Detail from "./Detail";
export default {
  name: "Result",

  components: {
    List,
    Detail
  }
};
</script>
<style lang="stylus" scoped></style>