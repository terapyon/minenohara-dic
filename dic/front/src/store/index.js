import Vue from "vue";
import Vuex from "vuex";
// import { Candidate } from "../models"
// import SearchService from "@/services/SearchService.js";
import ListServices from "@/services/ListServices.js"
import { Result } from "../models";


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
    SET_RESULT: function (state, candidate) {
      console.log(candidate)
      state.result = new Result(candidate.candidate, candidate.translate, candidate.word);
    },
    REMOVE_WORD: function (state) {
      state.word = ""
      state.candidates = []
    }
  },
  actions: {
    getCandidate({ commit }, word) {
      commit("SET_WORD", word);
      return ListServices.getList(word).then((candidates) => {
        commit("SET_CANDIDATES", candidates)
      });
    },
    // search({ commit }, word, data, mean) {
    //   return SearchService.postSearch(data, mean, word).then((res) => {
    //     commit("SET_RESULT", res)
    //   })
    // const result = SearchService.postSearch(word, data, mean)
    // return commit("SET_RESULT", result)
    // }
  },
  modules: {},
});
