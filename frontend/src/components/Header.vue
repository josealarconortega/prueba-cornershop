<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="primary">
      <b-container>
        <b-navbar-brand href="/">Cornershop</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-form><b> Menu </b></b-nav-form>
            <b-nav-item-dropdown right>
              <!-- Using 'button-content' slot -->
              <b-dropdown-item
                v-if="this.idUsuario > 0"
                href="#"
                @click="logout()"
                >Logout</b-dropdown-item
              >
              <b-dropdown-item v-if="this.idUsuario == 0" to="/Login"
                >Login</b-dropdown-item
              >
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </b-container>
    </b-navbar>
  </div>
</template>
<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
@Component
export default class Header extends Vue {
  idUsuario = 0;
  created() {
    if (localStorage.getItem("id_usuario") == null) {
      this.idUsuario = 0;
    } else {
      this.idUsuario = Number(localStorage.getItem("id_usuario"));
    }
  }
  logout() {
    localStorage.removeItem("id_usuario");
    window.location.reload();
  }
}
</script>
