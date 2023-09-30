<script>
import mirador from "mirador";
import DefaultLayout from "../components/DefaultLayout.vue";

export default {
  components: { DefaultLayout },
  props: {
    manifest: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      tify: null,
    };
  },
  mounted() {
    mirador.viewer({
      id: "mirador",
      windows: [{ manifestId: this.manifest, maximized: true }],
      window: {
        allowClose: false,
        defaultSideBarPanel: "annotations",
        sideBarOpenByDefault: true,
      },
      workspaceControlPanel: {
        enabled: false,
      },
    });
  },
};
</script>
<template>
  <div id="mirador" class="fixed w-screen" />
</template>
<style>
#mirador {
  height: calc(100vh - 80px);
}
</style>
