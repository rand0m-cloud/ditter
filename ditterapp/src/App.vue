<script setup>
import { RouterView } from "vue-router";
import { onMounted } from "vue";
import Header from "./components/Header.vue";
import API from "./API.js";

onMounted(() => {
  API.checkSessionStorage();
});
</script>

<template>
  <Header />
  <main>
    <RouterView />
  </main>
</template>
