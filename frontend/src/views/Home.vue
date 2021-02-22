<template>
  <div>
    <h1>Prueba Cornershop</h1>
    <Navbar></Navbar>

    <main>
      <div class="content-inside">
        <br />
        <PublicHome v-if="this.idUsuario == 0"></PublicHome>
        <PrivateHome v-if="this.idUsuario > 0"></PrivateHome>
      </div>
    </main>
    <Footer></Footer>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";

import Navbar from "@/components/Navbar.vue";
import PrivateHome from "@/components/PrivateHome.vue";
import PublicHome from "@/components/PublicHome.vue";
import Footer from "@/components/Footer.vue";

@Component({
  components: {
    Navbar,
    PrivateHome,
    PublicHome,
    Footer
  }
})
export default class Home extends Vue {
  idUsuario = 0;
  created() {
    if (localStorage.getItem("id_usuario") == null) {
      this.idUsuario = 0;
    } else {
      this.idUsuario = Number(localStorage.getItem("id_usuario"));
    }
  }
}
</script>
<style scoped>
body {
  margin-bottom: 170px;
  margin: 0;
  margin-bottom: 40px;
  padding-right: 0 !important;
}
html {
  min-height: 100%;
  position: relative;
  background: #ebebeb;
}
footer {
  position: absolute;
  bottom: 0;
  width: 100%;
}
main {
  margin: 50px;
}

small {
  font-size: 80%;
}
#app {
  font-family: "Open Sans", sans-serif;
  color: #606060;
  background: #ebebeb;
  text-align: center;
}
.breadcrumb {
  padding: 8px 15px;
  border: 1px solid #e7e7e7;
  margin: 10px 0px 20px;
  background-color: #fff;
}
a.nav-link {
  color: #ffffff;
}

#nav-link {
  color: #6c757d;
  font-size: 11px;
}
.nav-pills .nav-link.active,
.nav-pills .show > .nav-link {
  color: #fff;
  background-color: #5f9ed6;
}
.nav-pills .nav-link {
  border-radius: 0rem;
  padding: 0.8rem 1rem;
}
.nav-tabs .nav-link {
  color: #606060;
  border-color: #ebebeb;
}
.nav-tabs .nav-item.show .nav-link,
.nav-tabs .nav-link.active {
  color: #fff;
  background-color: #5f9ed6 !important;
  border-color: #4f94d2 !important;
}

.btn-primary,
.btn-primary:hover {
  color: #ffffff;
  background-color: #5f9ed6;
  border-color: #4f94d2;
}

.table thead {
  color: #ffffff;
  background-color: #428bca;
}

.table-hover tbody tr:hover td,
.table-hover tbody tr:hover th {
  color: #ffffff;
  background-color: #428bca;
}

.content-inside {
  padding-bottom: 120px;
}
.align-btn-rg {
  text-align: right;
  margin-right: 15px;
}
.align-btn-lf {
  text-align: left;
  margin-left: 15px;
}
.i-color {
  color: #4f94d2;
}
.msg-alert {
  width: 100%;
  margin-top: 0.25rem;
  font-size: 80%;
  color: #dc3545;
}
.msg-bold {
  font-weight: bold;
}
.titulo-fuente {
  font-size: 16px;
  font-weight: bold;
}
/*css wizard*/
.vue-form-wizard .wizard-header {
  padding: 0px;
}

.border-panel-card {
  border-top: 15px solid #5f9ed6;
}
.margin-top {
  position: relative;
  top: 12px;
}
.margin-left {
  position: relative;
  left: 10px;
}
.card-body {
  /*padding: 1rem;*/
  padding: 10px;
}
.small {
  max-width: 250px;
  margin: 0 auto;
}
.footer {
  background: #000000;
  color: #fff;
  border-color: #000000;
}
.azul {
  color: #5f9ed6;
}
.destacado {
  font-weight: bolder;
  font-size: 14px;
}
.destacadoTab {
  font-size: 17px;
}
.card-header {
  padding: 10px;
}
.nav-tabs .nav-item {
  background-color: white;
}
div.boxArea {
  height: 100px;
  width: 100%;
  overflow: auto;
  border: 1px solid #cccccc;
  background-color: #e9ecef;
  border-style: solid;
  border-width: 1px;
  border-color: #cccccc;
  border-radius: 5px;
  padding: 8px;
}
.swal2-container {
  z-index: 9999 !important;
  margin: 0;
}
.tabs /deep/ .tab-pane:focus {
  outline: none;
}
.swal2-container {
  zoom: 0.7;
}

.tamanio_titulo {
  font-size: 27px !important;
}

.custom-file-input.is-valid ~ .custom-file-label,
.was-validated {
  border-color: #5f9ed6 !important;
}
.custom-file-input.is-valid ~ .custom-file-label,
.was-validated .custom-file-input:valid ~ .custom-file-label {
  border-color: #5f9ed6 !important;
}
.custom-file-input.is-valid:focus ~ .custom-file-label,
.was-validated {
  border-color: #5f9ed6 !important;
}
.custom-file-input.is-valid:focus ~ .custom-file-label,
.was-validated .custom-file-input:valid:focus ~ .custom-file-label {
  border-color: #5f9ed6 !important;
  -webkit-box-shadow: 0 0 0 0.2rem rgba(40, 167, 69, 0.25);
  box-shadow: 0 0 0 0.2rem rgba(40, 121, 167, 0.25);
}

.bg-custom-1 {
  background-color: #5f9ed6 !important;
}
</style>
