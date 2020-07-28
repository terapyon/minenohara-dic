<template>
  <div>
    <v-row v-for="(candidate, index) in candidateList" :key="index">
      <v-col @click="showDetail(candidate.candidate, candidate.translate, candidate.word, index)">
        <v-card outlined :color="selected == index ? 'primary': ''">
          <v-list-item two-line>
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">{{ candidate.candidate }}</v-list-item-title>
              <v-list-item-subtitle>{{ candidate.translate }} / {{ candidate.word }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>
<script>
export default {
  name: "List",

  methods: {
    showDetail(candidate, translate, word, idx) {
      this.$store.commit("SET_RESULT", { candidate, translate, word });
      this.$store.commit("SET_SELECTED", idx);
    }
  },

  computed: {
    candidateList() {
      return this.$store.state.candidates;
    },
    selected() {
      return this.$store.state.selected;
    }
  }
};
</script>
<style lang="stylus" scoped></style>