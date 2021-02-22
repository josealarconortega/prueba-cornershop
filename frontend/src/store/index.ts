import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    alert: {
      message: "",
      type: ""
    },
    autenticate: false
  },
  mutations: {},
  actions: {},
  modules: {}
});
