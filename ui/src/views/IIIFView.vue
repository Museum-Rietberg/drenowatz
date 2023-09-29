<script>
import IIIFViewer from "../components/IIIFViewer.vue";
import DefaultLayout from "../components/DefaultLayout.vue";

export default {
  components: { DefaultLayout, IIIFViewer },
  computed: {
    manifest() {
      return `/manifests/${this.$route.params.id}.json`;
    },
  },
};
</script>

<template>
  <DefaultLayout narrow>
    <IIIFViewer :manifest="manifest" />
  </DefaultLayout>
</template>
