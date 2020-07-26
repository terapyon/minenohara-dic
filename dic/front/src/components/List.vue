<template>
  <div>
    <v-row v-for="i in [1, 2, 3]" :key="i" @click="showDetail(i)">{{ i }}</v-row>
    <input type="text" v-model="showWord" />
  </div>
</template>
<script>
export default {
  name: "List",

  methods: {
    showDetail(i) {
      this.$store.commit("SET_RESULT", i);
    }
  },

  computed: {
    showWord() {
      return this.$store.state.word;
    }
  }
};
</script>
<style lang="stylus" scoped></style>