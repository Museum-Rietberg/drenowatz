<script>
export default {
  props: {
    narrow: {
      type: Boolean,
      default: () => false,
    },
  },
};
</script>
<template>
  <div id="app" class="bg-black flex flex-col min-h-screen">
    <header class="bg-white px-8 py-4 flex justify-between">
      <router-link :to="{ name: 'overview' }" class="flex items-center">
        <img src="/logo.jpg" class="h-12 mr-4" />
        <h1 class="text-lg">drenowatz</h1>
      </router-link>
      <slot name="right" />
    </header>
    <main class="grow" :class="narrow ? '' : 'p-8'">
      <slot />
    </main>
  </div>
</template>
