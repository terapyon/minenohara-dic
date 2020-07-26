<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <h1>辞書アプリ</h1>
    </v-app-bar>

    <v-main>
      <Dic />
    </v-main>
  </v-app>
</template>

<script>
import Dic from "./components/Dic";

export default {
  name: "App",

  components: {
    Dic
  },

  data: () => ({
    //
  })
};
</script>
