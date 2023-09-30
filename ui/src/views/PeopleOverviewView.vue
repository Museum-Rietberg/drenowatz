<script>
import Card from "../components/Card.vue";
import DefaultLayout from "../components/DefaultLayout.vue";
import PersonFilter from "../components/PersonFilter.vue";
import PersonCard from "../components/PersonCard.vue";

export default {
  components: {PersonCard, Card, DefaultLayout, PersonFilter },
  async mounted() {
    const response = await fetch("https://fra1.digitaloceanspaces.com/drenowatz/people_overview.json");
    this.people = await response.json();
  },
  data() {
    return {
      people: [],
    };
  },
};
</script>

<template>
  <DefaultLayout>
    <template #right>
      <PersonFilter />
    </template>
    <div class="grid sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-8">
      <PersonCard v-for="person in people" v-bind="person" />
    </div>
  </DefaultLayout>
</template>
