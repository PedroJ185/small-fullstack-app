import { createRouter, createWebHistory } from "vue-router";
import users from "../views/users.vue";
import products from "../views/products.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", redirect: "/users" },
    { path: "/users", name: "users", component: users },
    { path: "/products", name: "products", component: products },
  ],
});

export default router;
