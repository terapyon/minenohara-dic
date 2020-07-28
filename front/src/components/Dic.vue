<template>
  <v-container>
    <InputWord />
    <Result />
  </v-container>
</template>
<script>
import InputWord from "./InputWord";
import Result from "./Result";
export default {
  name: "Dic",

  components: {
    InputWord,
    Result
  }
};
</script>
<style lang="stylus" scoped></style>