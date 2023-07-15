<script setup lang="ts">
import { RouterView } from "vue-router";
import { provide, ref, onMounted } from "vue";
import Header from "./components/Header.vue";

const user = ref(null);

onMounted(() => {
  const storedUser = sessionStorage.getItem("user");
  if (storedUser) {
    console.log(storedUser);
    user.value = JSON.parse(storedUser);
  }
});

provide("api_backend", "http://localhost:8000");
provide("user", user);
</script>

<template>
  <Header />
  <RouterView />
</template>
