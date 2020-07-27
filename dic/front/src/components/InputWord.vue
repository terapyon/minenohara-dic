<template>
  <v-row>
    <v-col cols="11">
      <v-text-field
        label="単語"
        placeholder="Type here..."
        @input="submitSearch"
        :value="searchWord"
      />
    </v-col>
    <v-col cols="1">
      <v-btn @click="removeWord">消す</v-btn>
    </v-col>
  </v-row>
</template>
<script>
export default {
  name: "InputWord",

  methods: {
    submitSearch(w) {
      this.$store
        .dispatch("getCandidate", w)
        .then(() => {
          this.$store.commit("SET_SELECTED", null);
        })
        .catch(() => {
          console.log("Error getList");
        });
    },
    removeWord() {
      this.$store.commit("SET_SELECTED", null);
      this.$store.commit("REMOVE_WORD");
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