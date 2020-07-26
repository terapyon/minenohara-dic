import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    word: "",
    candidate: [],
    result: "",
  },
  mutations: {
    SET_WORD: function(state, word) {
      state.word = word;
    },
    SET_RESULT: function(state, result) {
      state.result = result;
    },
  },
  actions: {},
  modules: {},
});
