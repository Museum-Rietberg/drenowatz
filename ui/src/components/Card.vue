<script>
export default {
  props: {
    id: {
      type: String,
      required: true,
    },
    thumbnail: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    artist: {
      type: String,
      required: true,
    },
  },
  computed: {
    thumbnailPath() {
      return "https://fra1.digitaloceanspaces.com/drenowatz" + this.thumbnail;
    },
  },
};
</script>

<template>
  <router-link
    :to="{ name: 'iiifview', params: { id } }"
    class="group max-w-sm rounded bg-white overflow-hidden flex flex-col"
  >
    <div class="overflow-hidden">
      <img
        class="w-full group-hover:scale-125 transition duration-200"
        :src="thumbnailPath"
      />
    </div>
    <div class="px-6 py-4 grow">
      <h2 class="font-bold text-xl mb-2">{{ title }}</h2>
    </div>
    <div class="px-6 pt-4 pb-2">
      <span
        class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
        >{{ artist }}</span
      >
    </div>
  </router-link>
</template>
