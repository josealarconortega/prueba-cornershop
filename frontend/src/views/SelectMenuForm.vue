<template>
  <div>
    <b-row>
      <b-col cols="9">
        <h3>
          Hola {{ this.name }}, selecciona el menu para la fecha {{ this.date }}
        </h3>
      </b-col>
    </b-row>
    <b-row>
      <b-col cols="9">
        <b-breadcrumb>Menu</b-breadcrumb>
        <b-row>
          <b-col cols="8">
            <b-form-group label="" label-for="menu">
              <b-form-select
                id="select-menu"
                v-model="selectMenu"
                :options="itemsMenus"
                required
              ></b-form-select>
            </b-form-group>
          </b-col>
          <b-col cols="4">
            <b-button
              v-if="hour <= 11 && isSelectMenu == 0"
              class="float-left btn-block btn-xs"
              type="button"
              variant="primary"
              @click="guardar()"
              >Guardar</b-button
            >
          </b-col>
        </b-row>
        <b-row>
          <b-col cols="8">
            <b-form-textarea
              id="textarea"
              v-model="observacion"
              placeholder="Ingrese especificaciones"
              rows="3"
              max-rows="6"
            ></b-form-textarea>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
  </div>
</template>
<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import api from "../services/api";
@Component
export default class SelectMenuForm extends Vue {
  usuarioId = 0;
  name = "";
  date = "";
  timestamp = ""; // eslint-disable-next-line
  itemsMenus = null as any // eslint-disable-next-line
  selectMenu = null as any
  observacion = "";
  isSelectMenu = 1;
  hour = 0;
  created() {
    this.getNow();
    if (this.hour > 11) {
      this.$store.state.alert = {
        message: "Hora no valida para seleccionar menu, se debe seleccionar antes de las 11",
        type: "info"
      };
    }
    api
      .get("usuarios/" + this.$route.params.uid + "/")
      .then(response => {
        if (response.status == 200) {
          this.name = response.data.data["nombre"];
          this.usuarioId = response.data.data["id"];
          this.listarMenu();
          this.getMenuSeleccionadosUsuario();
        } else {
          this.$store.state.alert = {
            message: "Error, link invalido",
            type: "danger"
          };
        }
      })
      .catch(() => {
        this.$store.state.alert = {
          message: "Error, link invalido",
          type: "danger"
        };
      });
  }
  getNow() {
    const today = new Date();
    const month =
      today.getMonth() + 1 < 10
        ? "0" + (today.getMonth() + 1)
        : today.getMonth() + 1;
    const date = today.getFullYear() + "-" + month + "-" + today.getDate();
    const time =
      today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    const dateTime = date + " " + time;
    this.date = today.getDate() + "-" + month + "-" + today.getFullYear();
    this.timestamp = dateTime;
    this.hour = today.getHours();
  }
  getMenuSeleccionadosUsuario() {
    api
      .post("usuarios/" + this.usuarioId + "/menus", {
        // eslint-disable-next-line
        user_id: this.usuarioId, // eslint-disable-next-line
        fecha_menu: this.timestamp
      })
      .then(response => {
        const dataMenus = response.data.data;
        if (response.data.status == 200) {
          if (dataMenus.length > 0) {
            this.$store.state.alert = {
              message: "Usuario ya selecciono menu",
              type: "info"
            };
            this.isSelectMenu = 1;
          } else {
            this.isSelectMenu = 0;
          }
        }
      })
      .catch(() => {
        this.$store.state.alert = {
          message: "Error al obtener los menus",
          type: "danger"
        };
        this.isSelectMenu = 1;
      });
  }

  listarMenu() {
    const itemsMenus = [{ text: "Seleccione menu", value: null }];
    api
      .post("menus/fecha/status", {
        fecha: this.timestamp,
        status: process.env.VUE_APP_STATUS_ID_CONFIRMADA
      })
      .then(response => {
        if (response.data.status == 200) {
          const dataMenus = response.data.data;
          let i = 1;
          for (const key in dataMenus) {
            const textMenu =
              "Opcion " +
              i +
              ", " +
              (dataMenus[key].entrada == ""
                ? ""
                : " entrada: " + dataMenus[key].entrada + "") +
              (dataMenus[key].plato_fondo == ""
                ? ""
                : " plato de fondo: " + dataMenus[key].plato_fondo + "") +
              (dataMenus[key].ensalada == ""
                ? ""
                : " ensalada: " + dataMenus[key].ensalada + "") +
              (dataMenus[key].postre == ""
                ? ""
                : " postre: " + dataMenus[key].postre + "");

            itemsMenus.push({
              value: dataMenus[key].id,
              text: textMenu
            });
            i += 1;
          }
          this.itemsMenus = itemsMenus;
        } else {
          this.$store.state.alert = {
            message: "Error al enviar los menus",
            type: "danger"
          };
          this.itemsMenus = itemsMenus;
        }
      })
      .catch(() => {
        this.$store.state.alert = {
          message: "Error al enviar los menus",
          type: "danger"
        };
        this.itemsMenus = itemsMenus;
      });
  }

  guardar() {
    if (this.selectMenu == null) {
      alert("Debe seleccionar un menu");
    } else {
      console.log(this.observacion);
      api
        .post("usuarios/reservar", {
          // eslint-disable-next-line
          user_id: this.usuarioId, // eslint-disable-next-line
          menu_id: this.selectMenu,
          observacion: this.observacion
        })
        .then(response => {
          if (response.data.status == 200) {
            this.isSelectMenu = 1;
            alert("Menu seleccionado correctamente");
          }
        })
        .catch(() => {
          this.$store.state.alert = {
            message: "Error al guardar los menus",
            type: "danger"
          };
        });
    }
  }
}
</script>
