<script setup>
import { RouterView, RouterLink } from "vue-router";
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
    <v-app-bar class="bg-orange">
      <v-app-bar-title>
        <RouterLink to="/" class="reset-link text-blue-darken-4">Ditter</RouterLink>
      </v-app-bar-title>
      <template v-slot:append>
        <div>
          <RouterLink
            v-if="!!API.user.value"
            :to="`/user/${API.user.value.author_username}`"
            class="reset-link"
          >
            <v-btn>{{ API.user.value.author_username }}</v-btn>
          </RouterLink>
          <v-btn v-if="login_status == `logged-in`" @click="logout">
            <v-icon>mdi-logout</v-icon>
          </v-btn>
          <v-btn v-if="login_status == `logged-out`" @click="login">
            <v-icon>mdi-login</v-icon>Login
          </v-btn>
        </div>
      </template>
    </v-app-bar>
    <v-main>
      <RouterView />
    </v-main>
  </v-app>
</template>
