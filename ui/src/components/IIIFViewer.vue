<script>
import "tify";
import "tify/dist/tify.css";
import DefaultLayout from "../components/DefaultLayout.vue";

export default {
  components: { DefaultLayout },
  props: {
    manifest: {
      type: String,
      required: true,
    },
  },
  beforeDestroy() {
    if (this.tify) {
      this.tify.destroy();
    }
  },
  methods: {
    hideControl(name) {
      document
        .querySelector(`button[aria-controls="${this.tify.app.getId(name)}"]`)
        .remove();
    },
  },
  data() {
    return {
      tify: null,
    };
  },
  mounted() {
    this.tify = new Tify({
      container: "#tify",
      manifestUrl: this.manifest,
    });
    this.tify.ready.then(() => {
      this.hideControl("info");
      this.hideControl("help");
    });
  },
};
</script>
<template>
  <div id="tify" style="height: calc(100vh - 80px)" />
</template>
