<script>
import DefaultLayout from "../components/DefaultLayout.vue";
import {S3_BUCKET, S3_ENDPOINT} from "../config";
export default {
  components: {DefaultLayout},
  computed: {
    data() {
      return `${S3_ENDPOINT}/${S3_BUCKET}/people/${this.$route.params.id}.json`;
    },
  },
};
</script>

<template>
  <DefaultLayout narrow>
    {{ data }}
  </DefaultLayout>
</template>
