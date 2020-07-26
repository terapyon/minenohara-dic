<template>
  <div>
    rrrrrrrrr
    <span>{{ getDetail }}</span>
  </div>
</template>
<script>
export default {
  name: "Detail",

  computed: {
    getDetail() {
      return this.$store.state.result;
    }
  }
};
</script>
<style lang="stylus" scoped></style>