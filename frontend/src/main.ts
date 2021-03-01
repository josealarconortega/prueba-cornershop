import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import BootstrapVue from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
Vue.config.productionTip = false; // eslint-disable-next-line
const rut = require("rut.js");

Vue.use(BootstrapVue);
Vue.use(rut);
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
