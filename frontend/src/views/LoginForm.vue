<template>
  <div id="login">
    <div class="h-100 bg-plum-plate-login bg-animation">
      <div class="d-flex h-100 justify-content-center align-items-center">
        <b-col md="8" class="mx-auto app-login-box">
          <div class="modal-dialog w-100 mx-auto">
            <div class="modal-content">
              <div class="modal-body">
                <div class="h5 modal-title text-center">
                  <h4 class="mt-2">
                    <div>Hola,</div>
                    <span>Ingresa tus credenciales.</span>
                  </h4>
                </div>
                <form ref="form">
                  <b-form-group id="rutGroup1" label-for="rutInput">
                    <b-form-input
                      id="rutInput"
                      type="text"
                      name="rut"
                      v-model="rut"
                      required
                      placeholder="Ingresa tu Rut"
                    >
                    </b-form-input>
                  </b-form-group>
                  <b-form-group id="passwordGroup2" label-for="password">
                    <b-form-input
                      id="password"
                      type="password"
                      name="password"
                      v-model="password"
                      required
                      placeholder="Ingresa tu Password"
                    >
                    </b-form-input>
                  </b-form-group>
                </form>
                <div class="divider" />
              </div>
              <div class="modal-footer clearfix">
                <div class="float-right">
                  <b-button variant="primary" @click="login" size="lg"
                    >Ingresar</b-button
                  >
                </div>
              </div>
            </div>
          </div>
        </b-col>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import api from "../services/api";
import rut from "rut.js";

@Component
export default class LoginForm extends Vue {
  rut = "";
  password = "";
  login() {
    if (this.rut && this.password) {
      if (!rut.validate(this.rut)) {
        alert("Ingrese rut valido");
      } else {
        const perfilId =
          process.env.VUE_APP_PERFIL_ID_MANTENIMIENTO == null
            ? ""
            : process.env.VUE_APP_PERFIL_ID_MANTENIMIENTO;
        api
          .post("usuarios/login", {
            rut: rut.format(this.rut),
            password: this.password, // eslint-disable-next-line
            perfil_id: parseInt(perfilId)
          })
          .then(response => {
            if (response.status == 200) {
              localStorage.setItem("id_usuario", response.data.data.id);
              window.location.href = "/";
            } else {
              this.$store.state.autenticate = false;
              this.$store.state.alert = {
                message: "Error al ingresar clave o rut",
                type: "danger"
              };
            }
          })
          .catch(() => {
            this.$store.state.autenticate = false;
            this.$store.state.alert = {
              message: "Error al ingresar clave o rut",
              type: "danger"
            };
          });
      }
    } else {
      this.$store.state.alert = {
        message: "Debe ingresar rut y contraseña",
        type: "danger"
      };
    }
  }
}
</script>
