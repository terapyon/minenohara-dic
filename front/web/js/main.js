var app = new Vue({
  el: "#app",
  mounted() {
    eel.return_hello()((message) => {
      this.message = message;
    });
  },
  data: {
    message: "",
  },
});
