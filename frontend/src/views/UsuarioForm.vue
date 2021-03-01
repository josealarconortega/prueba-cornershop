<template>
  <div>
    <b-row>
      <b-col cols="9">
        <h3>Usuarios</h3>
      </b-col>
    </b-row>
    <b-row>
      <b-col cols="9">
        <b-breadcrumb>Ingresar nuevo usuario.</b-breadcrumb>
        <b-row>
          <b-col cols="4">
            <b-form-group label="Rut" label-for="rut">
              <b-form-input
                type="text"
                v-model="rut"
                placeholder="Ingrese rut"
              ></b-form-input>
            </b-form-group>
          </b-col>
          <b-col cols="4">
            <b-form-group label="Nombre Completo" label-for="nombre">
              <b-form-input
                type="text"
                v-model="nombre"
                placeholder="Ingrese nombre completo"
              ></b-form-input>
            </b-form-group>
          </b-col>
          <b-col cols="4">
            <b-form-group
              id="select-perfil"
              label="Perfil:"
              label-for="input-3"
            >
              <b-form-select
                id="select-perfil"
                v-model="perfilId"
                :options="optionsPerfiles"
                required
              ></b-form-select>
            </b-form-group>
          </b-col>
        </b-row>
        <b-row>
          <b-col cols="4">
            <b-form-group
              label="Email (este debe ser el email registrado en slack)"
              label-for="nombre"
            >
              <b-form-input
                type="text"
                v-model="email"
                placeholder="Ingrese email"
              ></b-form-input>
            </b-form-group>
          </b-col>
          <b-col cols="4">
            <b-form-group label="Ingrese Contraseña" label-for="contrasenia">
              <b-form-input
                type="password"
                v-model="password"
                placeholder="Ingrese contrasenia"
              ></b-form-input>
            </b-form-group>
          </b-col>
          <b-col cols="4">
            <b-form-group
              label="Repita contraseña"
              label-for="repite_contrasenia"
            >
              <b-form-input
                type="password"
                v-model="password2"
                placeholder="Repita contraseña"
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
              @click="guardarActualizarUsuario()"
              ><div v-if="this.idUsuarioNew != 0">Editar</div>
              <div v-if="this.idUsuarioNew == 0">Guardar</div></b-button
            >
            <b-button
              v-if="this.idUsuarioNew != 0"
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
          <tr v-for="(item, index) in itemsUsuarios" :key="index">
            <td>{{ item.id }}</td>
            <td>{{ item.rut }}</td>
            <td>{{ item.nombre }}</td>
            <td>{{ item.email }}</td>
            <td>{{ item.perfilDescripcion }}</td>
            <td>{{ item.uid }}</td>
            <td>
              <a
                href="#"
                @click="
                  editarUsuario(
                    item.id,
                    item.rut,
                    item.nombre,
                    item.email,
                    item.perfilId
                  )
                "
                >Editar</a
              >
              - <a href="#" @click="eliminarUsuario(item.id)">Eliminar</a>
            </td>
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
import rut from "rut.js";

@Component({
  components: { DataTable }
})
export default class UsuariForm extends Vue {
  idUsuario = 0;
  idUsuarioNew = 0;
  rut = "";
  nombre = "";
  email = ""; // eslint-disable-next-line
  perfilId = null as any;
  password = "";
  password2 = "";
  timestamp = "";
  date = ""; // eslint-disable-next-line
  itemsUsuarios = null as any; // eslint-disable-next-line
  optionsPerfiles = null as any;
  dataHeaders = [
    "Id",
    "Rut",
    "Nombre",
    "Email",
    "Perfil descripcion",
    "Uid",
    "Acción"
  ];
  created() {
    if (localStorage.getItem("id_usuario") == null) {
      this.idUsuario = 0;
      this.$router.push({ name: "Home" });
    } else {
      this.idUsuario = Number(localStorage.getItem("id_usuario"));
    }
    this.getNow();
    this.listarUsuarios();
    this.getPerfil();
  }
  clearForm() {
    this.idUsuarioNew = 0;
    this.rut = "";
    this.nombre = "";
    this.email = "";
    this.perfilId = null;
    this.password = "";
    this.password2 = "";
  }

  editarUsuario(
    id: number,
    rut: string,
    nombre: string,
    email: string,
    perfilId: number
  ) {
    this.idUsuarioNew = id;
    this.rut = rut;
    this.nombre = nombre;
    this.email = email;
    this.perfilId = perfilId;
  }
  guardarActualizarUsuario() {
    if (this.idUsuario == 0) {
      alert("Sesion caducada");
    } else if (this.rut == "") {
      alert("Ingrese rut");
    } else if (!rut.validate(this.rut)) {
      alert("Ingrese rut valido");
    } else if (this.nombre == "") {
      alert("Ingrese nombre");
    } else if (this.email == "") {
      alert("Ingrese email");
    } else if (this.perfilId == null) {
      alert("Seleccione perfil");
    } else if (this.password == "") {
      alert("Seleccione contraseña");
    } else if (this.password != this.password2) {
      alert("Contraseñas deben ser iguales");
    } else {
      let url = "usuarios/crear";
      const usuarioData = {
        rut: rut.format(this.rut),
        nombre: this.nombre,
        email: this.email, // eslint-disable-next-line
        perfil_id: this.perfilId,
        password: this.password, // eslint-disable-next-line
        usuario_id: this.idUsuarioNew,
      };
      if (this.idUsuarioNew > 0) {
        url = "usuarios/editar";
      } else {
        delete usuarioData.usuario_id;
      }
      api
        .post(url, usuarioData)
        .then(response => {
          if (response.status == 200) {
            this.clearForm();
            this.listarUsuarios();
            this.$store.state.alert = {
              message: "Usuario creado exitosamente",
              type: "success"
            };
          } else {
            this.$store.state.alert = {
              message: "Error al crear el usuario",
              type: "danger"
            };
          }
        })
        .catch(() => {
          this.$store.state.alert = {
            message: "Error al crear el usuario",
            type: "danger"
          };
        });
    }
  }

  listarUsuarios() {
    api
      .get("usuarios")
      .then(response => {
        if (response.data.status == 200) {
          const dataUsuarios = response.data.data;
          const itemsUsuarios = [];
          for (const key in dataUsuarios) {
            itemsUsuarios.push({
              id: dataUsuarios[key].id,
              rut: dataUsuarios[key].rut,
              nombre: dataUsuarios[key].nombre,
              email: dataUsuarios[key].email,
              uid: dataUsuarios[key].uid, // eslint-disable-next-line
              perfilId: dataUsuarios[key].perfil_id,// eslint-disable-next-line
              perfilDescripcion: dataUsuarios[key].perfil_descripcion
            });
          }
          this.itemsUsuarios = itemsUsuarios;
        } else {
          this.$store.state.alert = {
            message: "Error al enviar los usuarios",
            type: "danger"
          };
        }
      })
      .catch(() => {
        this.$store.state.alert = {
          message: "Error al enviar los usuarios",
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
  }

  eliminarUsuario(id: number) {
    api
      .delete("usuarios/eliminar/" + id, {})
      .then(response => {
        if (response.status == 200) {
          this.listarUsuarios();
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

  getPerfil() {
    api
      .get("perfiles")
      .then(response => {
        if (response.status == 200) {
          const dataPerfil = response.data.data;
          const itemsPerfil = [{ value: null, text: "Seleccione Perfil" }];
          for (const key in dataPerfil) {
            itemsPerfil.push({
              value: dataPerfil[key].id,
              text: dataPerfil[key].descripcion
            });
          }
          this.optionsPerfiles = itemsPerfil;
        }
      })
      .catch(() => {
        this.$store.state.alert = {
          message: "Error al obtener perfiles",
          type: "danger"
        };
      });
  }
}
</script>
