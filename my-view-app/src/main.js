import { createApp } from "vue";
import App from "./App.vue";
import "./assets/main.css";
import UserRegistration from "./components/UserRegistration/UserRegistration.vue";
import Login from "./components/Login/Login.vue";
import Dashboard from "./components/Dashboard/Dashboard.vue";
import { createRouter, createWebHistory } from "vue-router";

const routes = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "dashboard",
      component: Dashboard,
    },
    {
      path: "/register",
      name: "registration",
      component: UserRegistration,
    },
    {
      path: "/login",
      name: "login",
      component: Login,
    },
  ],
});
createApp(App).use(routes).mount("#app");
