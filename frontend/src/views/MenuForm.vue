<template>
  <div>
    <b-row>
      <b-col cols="4">
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
          @click="buscarMenuFecha()"
        >
          Buscar
        </b-button>
      </b-col>
    </b-row>
    <b-row>
      <b-col cols="12">
        <h3>Menu para la fecha {{ this.date }}</h3>
      </b-col>
    </b-row>
    <b-row>
      <b-col cols="12">
        <b-breadcrumb>Ingresar nuevo menu.</b-breadcrumb>
        <b-row>
          <b-col cols="4">
            <b-form-group label="Descripcion" label-for="descripcion">
              <b-form-input
                type="text"
                v-model="descripcion"
                placeholder="Ingrese descripcion"
              ></b-form-input>
            </b-form-group>
          </b-col>
          <b-col cols="4">
            <b-form-group label="Entrada" label-for="entrada">
              <b-form-input
                type="text"
                v-model="entrada"
                placeholder="Ingrese entrada"
              ></b-form-input>
            </b-form-group>
          </b-col>
          <b-col cols="4">
            <b-form-group label="Ensalada" label-for="ensalada">
              <b-form-input
                type="text"
                v-model="ensalada"
                placeholder="Ingrese ensalada"
              ></b-form-input>
            </b-form-group>
          </b-col>
        </b-row>
        <b-row>
          <b-col cols="4">
            <b-form-group label="Plato de Fondo" label-for="platoFondo">
              <b-form-input
                type="text"
                v-model="platoFondo"
                placeholder="Ingrese plato de fondo"
              ></b-form-input>
            </b-form-group>
          </b-col>
          <b-col cols="4">
            <b-form-group label="Postre" label-for="postre">
              <b-form-input
                type="text"
                v-model="postre"
                placeholder="Ingrese plato de fondo"
              ></b-form-input>
            </b-form-group>
          </b-col>
        </b-row>
        <b-row>
          <b-col cols="6">
            <b-button
              class="float-left"
              type="button"
              variant="primary"
              @click="guardarActualizarMenu()"
              ><div v-if="this.idMenu != 0">Editar</div>
              <div v-if="this.idMenu == 0">Guardar</div></b-button
            >
            <b-button
              v-if="this.idUsuario != 0"
              class="float-left"
              type="button"
              variant="danger"
              @click="clearForm()"
              >Limpiar</b-button
            >
          </b-col>
        </b-row>
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
          <tr v-for="(item, index) in itemsMenus" :key="index">
            <td>{{ item.opcion }}</td>
            <td>{{ item.descripcion }}</td>
            <td>{{ item.entrada }}</td>
            <td>{{ item.ensalada }}</td>
            <td>{{ item.platoFondo }}</td>
            <td>{{ item.postre }}</td>
            <td>{{ item.status }}</td>
            <td>
              <a
                href="#"
                @click="
                  editarMenu(
                    item.id,
                    item.descripcion,
                    item.entrada,
                    item.ensalada,
                    item.platoFondo,
                    item.postre
                  )
                "
                >Editar</a
              >
              - <a href="#" @click="eliminarMenu(item.id)">Eliminar</a>
            </td>
          </tr>
        </template>
      </DataTable>
    </b-row>
    <b-row>
      <b-col cols="6" offset="3">
        <b-button
          class="float-left"
          type="button"
          variant="primary btn-block"
          @click="confirmarMenu()"
          v-if="botonConfirmarVisible == 1"
          >Enviar y confirmar Menu</b-button
        >
      </b-col>
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
export default class MenuForm extends Vue {
  idMenu = 0;
  idUsuario = 0;
  descripcion = "";
  entrada = "";
  ensalada = "";
  platoFondo = "";
  postre = "";
  fechaMenu = "";
  initialDate = "";
  fechaMenuDMY = "";
  date = "";
  dataHeaders = [
    "Opcion",
    "Descripcion",
    "Entrada",
    "Ensalada",
    "Plato Fondo",
    "Postre",
    "Status",
    "Acción"
  ];
  timestamp = ""; // eslint-disable-next-line
  itemsMenus = null as any;
  botonConfirmarVisible = 1;
  created() {
    if (localStorage.getItem("id_usuario") == null) {
      this.idUsuario = 0;
      this.$router.push({ name: "Home" });
    } else {
      this.idUsuario = Number(localStorage.getItem("id_usuario"));
    }
    this.getNow();
    this.listarMenu();
  }
  openDate() {
    // eslint-disable-next-line
    const fecha = window.document.getElementById("fecha_menu")!;
    fecha.click();
  }
  buscarMenuFecha() {
    this.date = this.fechaMenuDMY;
    this.timestamp = moment(this.fechaMenu).format("YYYY-MM-DD HH:mm:ss");
    this.listarMenu();
  }
  clearForm() {
    this.idMenu = 0;
    this.descripcion = "";
    this.entrada = "";
    this.ensalada = "";
    this.platoFondo = "";
    this.postre = "";
  } // eslint-disable-next-line
  onContext(ctx: any) {
    if (ctx.selectedYMD == "") {
      this.fechaMenuDMY = moment(this.initialDate).format("DD-MM-YYYY");
    } else {
      this.fechaMenuDMY = moment(ctx.selectedYMD).format("DD-MM-YYYY");
    }
  }
  editarMenu(
    id: number,
    descripcion: string,
    entrada: string,
    ensalada: string,
    platoFondo: string,
    postre: string
  ) {
    this.idMenu = id;
    this.descripcion = descripcion;
    this.entrada = entrada;
    this.ensalada = ensalada;
    this.platoFondo = platoFondo;
    this.postre = postre;
  }
  guardarActualizarMenu() {
    if (localStorage.getItem("id_usuario") == null) {
      this.idUsuario = 0;
    } else {
      this.idUsuario = Number(localStorage.getItem("id_usuario"));
    }
    if (this.idUsuario == 0) {
      alert("Sesion caducada");
    } else if (this.descripcion == "") {
      alert("Ingrese descripcion");
    } else if (this.platoFondo == "") {
      alert("Ingrese plato de fondo");
    } else {
      const statusId =
        process.env.VUE_APP_STATUS_ID_REGISTRADA == null
          ? ""
          : process.env.VUE_APP_STATUS_ID_REGISTRADA;

      let url = "menus/crear";
      // eslint-disable
      const menusData = {
        descripcion: this.descripcion,
        entrada: this.entrada,
        ensalada: this.ensalada, // eslint-disable-next-line
        plato_fondo: this.platoFondo,
        postre: this.postre, // eslint-disable-next-line
        fecha_menu: this.timestamp, // eslint-disable-next-line
        status_id: parseInt(statusId), // eslint-disable-next-line
        menu_id: this.idMenu
      };
      if (this.idMenu > 0) {
        url = "menus/editar";
        menusData["menu_id"] = this.idMenu;
      } else {
        delete menusData.menu_id;
      }
      api
        .post(url, {
          // eslint-disable-next-line
          user_id: this.idUsuario,
          menus: [menusData]
        })
        .then(response => {
          if (response.status == 200) {
            this.listarMenu();
            this.clearForm();
          } else {
            this.$store.state.alert = {
              message: "Error al crear el menu",
              type: "danger"
            };
          }
        })
        .catch(() => {
          this.$store.state.alert = {
            message: "Error al crear el menu",
            type: "danger"
          };
        });
    }
  }

  listarMenu() {
    api
      .post("menus/fecha", {
        fecha: this.timestamp
      })
      .then(response => {
        if (response.data.status == 200) {
          const dataMenus = response.data.data;
          const itemsMenus = [];
          let i = 1;
          let flag = 0;
          for (const key in dataMenus) {
            itemsMenus.push({
              opcion: "Opcion " + i,
              id: dataMenus[key].id,
              descripcion: dataMenus[key].descripcion,
              entrada: dataMenus[key].entrada,
              ensalada: dataMenus[key].ensalada, // eslint-disable-next-line
              platoFondo: dataMenus[key].plato_fondo,
              postre: dataMenus[key].postre, // eslint-disable-next-line
              status_id:  dataMenus[key].status_id,
              status: dataMenus[key].status_descripcion,
              orden: dataMenus[key].orden
            }); // eslint-disable-next-line
            if (dataMenus[key].status_id == process.env.VUE_APP_STATUS_ID_CONFIRMADA) {
              flag = 1;
            }
            i += 1;
          }
          if (flag == 1) {
            this.botonConfirmarVisible = 0;
            this.$store.state.alert = {
              message: "No se puede volver a confirmar un menu ya enviado",
              type: "info"
            };
          } else if (i == 1) {
            this.botonConfirmarVisible = 0;
            this.$store.state.alert = {
              message: "No existen menus",
              type: "info"
            };
          }
          this.itemsMenus = itemsMenus;
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
  confirmarMenu() {
    const statusId =
      process.env.VUE_APP_STATUS_ID_CONFIRMADA == null
        ? ""
        : process.env.VUE_APP_STATUS_ID_CONFIRMADA;
    const perfilId =
      process.env.VUE_APP_PERFIL_ID_EMPLEADO == null
        ? ""
        : process.env.VUE_APP_PERFIL_ID_EMPLEADO;
    const menus = [];
    let flag = 0;
    for (const key in this.itemsMenus) {
      menus.push(this.itemsMenus[key].id); // eslint-disable-next-line
      if (this.itemsMenus[key].status_id == process.env.VUE_APP_STATUS_ID_CONFIRMADA) {
        flag = 1;
      }
    }
    if (flag == 0) {
      api
        .post("menus/confirmar", {
          // eslint-disable-next-line
              perfil_id: parseInt(perfilId),// eslint-disable-next-line
              menu_ids: menus,// eslint-disable-next-line
              status_id: parseInt(statusId)
        })
        .then(response => {
          if (response.status == 200) {
            this.listarMenu();
          } else {
            this.$store.state.alert = {
              message: response.data.message,
              type: "danger"
            };
          }
        })
        .catch(() => {
          this.$store.state.alert = {
            message: "Error al enviar la solicitud",
            type: "danger"
          };
        });
    } else {
      alert("Menu ya fue enviado");
    }
  }
  getNow() {
    const today = new Date();
    this.timestamp = moment(String(today.toString())).format(
      "YYYY-MM-DD HH:mm:ss"
    );
    this.initialDate = moment(String(today.toString())).format("YYYY-MM-DD");
    this.date = moment(String(today.toString())).format("DD-MM-YYYY");
    this.fechaMenu = moment(String(today.toString())).format("YYYY-MM-DD");
  }

  eliminarMenu(id: number) {
    api
      .delete("menus/eliminar/" + id, {})
      .then(response => {
        if (response.status == 200) {
          this.listarMenu();
          this.$store.state.alert = {
            message: "Eliminado correctamente",
            type: "success"
          };
        } else {
          this.$store.state.alert = {
            message: "Error",
            type: "danger"
          };
        }
      })
      .catch(() => {
        this.$store.state.alert = {
          message: "Error al enviar la solicitud",
          type: "danger"
        };
      });
  }
}
</script>
