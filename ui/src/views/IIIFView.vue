<script>
import IIIFViewer from "../components/IIIFViewer.vue";
import DefaultLayout from "../components/DefaultLayout.vue";
import { S3_ENDPOINT, S3_BUCKET } from "../config";

export default {
  components: { DefaultLayout, IIIFViewer },
  computed: {
    manifest() {
      return `${S3_ENDPOINT}/${S3_BUCKET}/manifests/${this.$route.params.id}.json`;
    },
  },
};
</script>

<template>
  <DefaultLayout narrow>
    <IIIFViewer :manifest="manifest" />
  </DefaultLayout>
</template>
