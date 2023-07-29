<script setup>
import { RouterView } from "vue-router";
import { onMounted, computed } from "vue";
import API from "./API.js";
import router from "./router";

onMounted(() => {
  API.checkSessionStorage();
});

const login_status = computed(() => {
  if (API.user.value) {
    return "logged-in";
  } else {
    return "logged-out";
  }
});

const logout = () => API.logout();
const login = () => router.push("/login");
</script>

<template>
  <v-app>
    <v-app-bar class="bg-orange" title="Ditter">
      <template v-slot:append>
        <v-btn v-if="login_status == `logged-in`" @click="logout">
          <v-icon>mdi-logout</v-icon>Logout
        </v-btn>
        <v-btn v-if="login_status == `logged-out`" @click="login">
          <v-icon>mdi-login</v-icon>Login
        </v-btn>
      </template>
    </v-app-bar>
    <v-main>
      <RouterView />
    </v-main>
  </v-app>
</template>
