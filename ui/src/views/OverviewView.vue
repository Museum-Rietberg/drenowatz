<script>
import Card from "../components/Card.vue";
import DefaultLayout from "../components/DefaultLayout.vue";
import PersonFilter from "../components/PersonFilter.vue";

export default {
  components: { Card, DefaultLayout, PersonFilter },
  async mounted() {
    const response = await fetch(
      "https://fra1.digitaloceanspaces.com/drenowatz/overview.json"
    );
    this.paintings = await response.json();
  },
  data() {
    return {
      paintings: [],
    };
  },
};
</script>

<template>
  <DefaultLayout>
    <template #right>
      <PersonFilter />
    </template>
    <div class="grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8">
      <Card v-for="painting in paintings" v-bind="painting" />
    </div>
  </DefaultLayout>
</template>
