import Vue from "vue";
import Vuex from "vuex";
// import { Candidate } from "../models"
import SearchService from "@/services/SearchService.js";
import ListServices from "@/services/ListServices.js"


Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    word: "",
    candidates: [],
    selected: null,
    result: null,
  },
  mutations: {
    SET_WORD: function (state, word) {
      state.word = word;
    },
    SET_CANDIDATES: function (state, candidates) {
      state.candidates = candidates
    },
    SET_SELECTED: function (state, idx) {
      state.selected = idx
    },
    SET_RESULT: function (state, result) {
      state.result = result;
    },
    REMOVE_WORD: function (state) {
      state.word = ""
    }
  },
  actions: {
    getCandidate({ commit }, word) {
      const candidates = ListServices.getList(word)
      return commit("SET_CANDIDATES", candidates)
    },
    search({ commit }, word) {
      // return SearchService.postSearch(word).then((res) => {
      //   commit("SET_RESULT", res)
      // })
      const result = SearchService.postSearch(word)
      return commit("SET_RESULT", result)
    }
  },
  modules: {},
});
