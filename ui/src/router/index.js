import Vue from "vue";
import VueRouter from "vue-router";
import IIIFView from "../views/IIIFView.vue";
import OverviewView from "../views/OverviewView.vue";
import PeopleOverviewView from "../views/PeopleOverviewView.vue";

Vue.use(VueRouter);

const router = new VueRouter({
  mode: "history",
  base: import.meta.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "overview",
      component: OverviewView,
    },
    {
      path: "/iiif/:id",
      name: "iiifview",
      component: IIIFView,
    },
    {
      path: "/people",
      name: "people_overview",
      component: PeopleOverviewView,
    },
  ],
});

export default router;
