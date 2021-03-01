import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import Home from "../views/Home.vue";
import LoginForm from "../views/LoginForm.vue";
import UsuarioForm from "../views/UsuarioForm.vue";
import MenuForm from "../views/MenuForm.vue";
import SelectMenuForm from "../views/SelectMenuForm.vue";
import UsuariosMenuForm from "../views/UsuariosMenuForm.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/login",
    name: "Login",
    component: LoginForm
  },
  {
    path: "/usuario",
    name: "Usuario",
    component: UsuarioForm
  },
  {
    path: "/menu",
    name: "Menu",
    component: MenuForm
  },
  {
    path: "/menu/:uid",
    name: "Menu",
    component: SelectMenuForm
  },
  {
    path: "/usuariosmenu",
    name: "UsuariosMenu",
    component: UsuariosMenuForm
  }
];

const router = new VueRouter({
  routes
});

export default router;
