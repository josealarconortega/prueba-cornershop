<template>
  <div>
    <b-row>
      <b-col cols="8">
        <b-input-group class="mb-3">
          <b-form-input
            size="sm"
            id="input_fecha_menu"
            readonly
            v-model="fechaMenuDMY"
            type="text"
            placeholder="DD-MM-YYYY"
            autocomplete="off"
            v-on:click="openDate()"
          ></b-form-input>
          <b-input-group-append>
            <b-form-datepicker
              size="sm"
              v-model="fechaMenu"
              button-only
              right
              locale="es"
              id="fecha_menu"
              :initial-date="initialDate"
              aria-controls="input_fecha_menu"
              @context="onContext"
            ></b-form-datepicker>
          </b-input-group-append>
        </b-input-group>
      </b-col>
      <b-col cols="4">
        <b-button
          class="btn-block btn-sm"
          type="button"
          variant="primary"
          @click="buscarUsuarioMenuFecha()"
        >
          Buscar
        </b-button>
      </b-col>
    </b-row>
    <b-row>
      <b-col cols="12">
        <h3>
          Menus seleccionados por los usuarios para la fecha {{ this.date }}
        </h3>
      </b-col>
    </b-row>
    <b-row>
      <DataTable
        :title="'Lista Menus'"
        :headers="dataHeaders"
        :dt="'list_menus'"
        :incard="false"
      >
        <template slot="table_data">
          <tr v-for="(item, index) in itemsUsuarioMenus" :key="index">
            <td>{{ item.rutUsuario }}</td>
            <td>{{ item.nombre }}</td>
            <td>{{ item.descripcionMenu }}</td>
            <td>{{ item.entrada }}</td>
            <td>{{ item.ensalada }}</td>
            <td>{{ item.platoFondo }}</td>
            <td>{{ item.postre }}</td>
          </tr>
        </template>
      </DataTable>
    </b-row>
  </div>
</template>
<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import api from "../services/api";
import DataTable from "@/components/DataTable.vue";
import moment from "moment";

@Component({
  components: { DataTable }
})
export default class UsuariosMenuForm extends Vue {
  fechaMenu = "";
  initialDate = "";
  fechaMenuDMY = "";
  date = "";
  idUsuario = 0;
  timestamp = "";
  dataHeaders = [
    "Rut Usuario",
    "Nombre Usuario",
    "Descripcion menu",
    "Entrada",
    "Ensalada",
    "Plato Fondo",
    "Postre"
  ]; // eslint-disable-next-line
  itemsUsuarioMenus = null as any;
  created() {
    if (localStorage.getItem("id_usuario") == null) {
      this.idUsuario = 0;
      this.$router.push({ name: "Home" });
    } else {
      this.idUsuario = Number(localStorage.getItem("id_usuario"));
    }
    this.getNow();
    this.listarUsuarioMenu();
  }
  getNow() {
    const today = new Date();
    this.timestamp = moment(String(today.toString())).format(
      "YYYY-MM-DD HH:mm:ss"
    );
    this.initialDate = moment(String(today.toString())).format("YYYY-MM-DD");
    this.date = moment(String(today.toString())).format("DD-MM-YYYY");
    this.fechaMenu = moment(String(today.toString())).format("YYYY-MM-DD");
  } // eslint-disable-next-line
  onContext(ctx: any) {
    if (ctx.selectedYMD == "") {
      this.fechaMenuDMY = moment(this.initialDate).format("DD-MM-YYYY");
    } else {
      this.fechaMenuDMY = moment(ctx.selectedYMD).format("DD-MM-YYYY");
    }
  }
  openDate() {
    // eslint-disable-next-line
    const fecha = window.document.getElementById("fecha_menu")!;
    fecha.click();
  }
  listarUsuarioMenu() {
    api
      .post("usuarios/menus", {
        // eslint-disable-next-line
        fecha_menu: this.timestamp
      })
      .then(response => {
        if (response.data.status == 200) {
          const dataUsuarioMenus = response.data.data;
          const itemsUsuarioMenus = [];
          for (const key in dataUsuarioMenus) {
            itemsUsuarioMenus.push({
              rutUsuario: dataUsuarioMenus[key].usuario.rut,
              nombre: dataUsuarioMenus[key].usuario.nombre,
              descripcionMenu: dataUsuarioMenus[key].menu.descripcion,
              entrada: dataUsuarioMenus[key].menu.entrada,
              ensalada: dataUsuarioMenus[key].menu.ensalada, // eslint-disable-next-line
              platoFondo: dataUsuarioMenus[key].menu.plato_fondo,
              postre: dataUsuarioMenus[key].menu.postre
            });
          }
          this.itemsUsuarioMenus = itemsUsuarioMenus;
        } else {
          this.$store.state.alert = {
            message: "Error al enviar los menus",
            type: "danger"
          };
        }
      })
      .catch(() => {
        this.$store.state.alert = {
          message: "Error al enviar los menus",
          type: "danger"
        };
      });
  }
  buscarUsuarioMenuFecha() {
    this.date = this.fechaMenuDMY;
    this.timestamp = moment(this.fechaMenu).format("YYYY-MM-DD HH:mm:ss");
    this.listarUsuarioMenu();
  }
}
</script>
