<template>
  <div v-if="alert.message" data-test="alert-wraper">
    <v-alert
      v-model="isAlert"
      :type="alert.type"
      close-text="Cerrar"
      dismissible
      @input="clear()"
    >
      {{ alert.message }}
    </v-alert>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import { mapState } from "vuex";
@Component({
  computed: mapState(["alert"])
})
export default class Alert extends Vue {
  isAlert = true;

  updated() {
    this.isAlert = this.$store.state.alert.message ? true : false;
    if (this.isAlert) {
      window.scrollTo(0, 0);
    }
  }

  clear() {
    this.$store.state.alert = {
      message: "",
      type: ""
    };
  }
}
</script>
