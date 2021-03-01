import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    alert: {
      message: "",
      type: ""
    },
    key: "",
    autenticate: false
  },
  mutations: {},
  actions: {},
  modules: {}
});
