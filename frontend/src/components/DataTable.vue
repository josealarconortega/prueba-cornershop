<template>
  <b-col cols="12">
    <div :class="{ loading: loading }" style="overflow-x:auto;">
      <br />
      <table :id="dt" class="display table nowrap table-striped table-bordered">
        <thead>
          <tr>
            <th :data-test="dataTest" v-for="item in headers" :key="item.index">
              {{ item }}
            </th>
          </tr>
        </thead>
        <tbody>
          <slot name="table_data">
            <!-- Idem anterior -->
          </slot>
        </tbody>
      </table>
    </div>
  </b-col>
</template>
<script lang="ts">
import { Vue, Component, Prop } from "vue-property-decorator";
import $ from "jquery";
import "datatables.net";
import "datatables.net-dt";
import "datatables.net-buttons";
import "datatables.net-buttons-bs4";
import "datatables.net-buttons/js/buttons.html5.js";
import "datatables.net-bs4/css/dataTables.bootstrap4.css";
import "datatables.net-bs4/js/dataTables.bootstrap4.js";
@Component({
  components: {}
})
/* eslint-disable */
export default class DataTable extends Vue { 
  @Prop() title: any; // Titulo de la DataTable , esto se dibuja solamente si usas la version con b-card
  @Prop() headers: any; // Cabeceras de la DataTable , array
  @Prop() incard: any; // Booleano , indica si la datatable se envuelve o no en una etiqueta b-card
  @Prop() dt: any; // Id de la DataTable
  dataTable = null as any;
  loading = false;
  dataTest = "table_headers_" + this.dt;
  mounted() {
    this.createTable();
  }
  async beforeUpdate() {
    await this.dataTable.destroy();
    this.createTable();
  }
  createTable() {
    this.dataTable = $("#" + this.dt).DataTable({
      language: {
        processing: "Procesando...",
        lengthMenu: "Mostrar _MENU_ registros",
        zeroRecords: "No se encontraron resultados",
        emptyTable: "Ningún dato disponible en esta tabla",
        info:
          "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
        infoEmpty: "Mostrando registros del 0 al 0 de un total de 0 registros",
        infoFiltered: "(filtrado de un total de _MAX_ registros)",
        infoPostFix: "",
        search: "Buscar:",
        url: "",
        thousands: ",",
        loadingRecords: "Cargando...",
        paginate: {
          first: "Primero",
          last: "Último",
          next: "Siguiente",
          previous: "Anterior"
        },
        aria: {
          sortAscending:
            ": Activar para ordenar la columna de manera ascendente",
          sortDescending:
            ": Activar para ordenar la columna de manera descendente"
        }
      },
      dom: "lfBrtip",
      buttons: [
        {
          extend: "csv",
          text: "Exportar a CSV",
          className: "btn btn-default btn-sm test-export-button-" + this.dt
        }
      ],
      lengthMenu: [
        [100, 200, 300, 500, 1000, 5000, -1],
        [100, 200, 300, 500, 1000, 5000, "Todos"]
      ]
    });
  }
}
</script>
<style>
.dataTables_filter {
  text-align: left !important;
}
</style>
