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
    name: {
      type: String,
      required: true,
    },
    number_seals: {
      type: Number,
      required: true,
    },
    number_works_painted: {
      type: Number,
      required: true,
    },
    number_works_sealed: {
      type: Number,
      required: true,
    },
  },
};
</script>

<template>
  <router-link
    :to="{ name: 'personview', params: { id } }"
    class="max-w-sm rounded bg-white overflow-hidden"
  >
    <img class="w-full" :src="thumbnail" />
    <div class="px-6 py-4">
      <div class="font-bold text-xl mb-2">{{ title }}</div>
    </div>
    <div class="px-6 pt-4 pb-2">
      <span
        class="block px-3 py-1 text-sm font-bold text-gray-700 mr-2 mb-2"
        >{{ name }}</span
      >
      <span
        class="inline-block px-3 py-1 text-sm text-gray-700 mr-2 mb-2"
        >Painted {{ number_works_painted }} works</span
      >
      <span
        class="inline-block px-3 py-1 text-sm text-gray-700 mr-2 mb-2"
        >Placed seal on {{ number_works_sealed }} works</span
      >
      <span
        class="inline-block px-3 py-1 text-sm text-gray-700 mr-2 mb-2"
        >Used {{ number_seals }} different seals</span
      >
    </div>
  </router-link>
</template>
