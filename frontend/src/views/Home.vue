<template>
  <div>
    <center><h1>Prueba Cornershop</h1></center>
    <main>
      <br />
      <PublicHome v-if="this.idUsuario == 0"></PublicHome>
      <PrivateHome v-if="this.idUsuario > 0"></PrivateHome>
    </main>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";

import PrivateHome from "@/components/PrivateHome.vue";
import PublicHome from "@/components/PublicHome.vue";

@Component({
  components: {
    PrivateHome,
    PublicHome
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
