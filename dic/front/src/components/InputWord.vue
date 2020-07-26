<template>
  <v-row>
    <v-col cols="10">
      <v-text-field
        label="単語"
        placeholder="Type here..."
        @input="submitSearch"
        :value="searchWord"
      />
    </v-col>
    <v-col cols="2">
      <v-btn>検索</v-btn>
    </v-col>
  </v-row>
</template>
<script>
export default {
  name: "InputWord",

  methods: {
    submitSearch(w) {
      this.$store.commit("SET_WORD", w);
    }
  },

  computed: {
    searchWord() {
      return this.$store.state.word;
    }
  }
};
</script>
<style lang="stylus" scoped></style>