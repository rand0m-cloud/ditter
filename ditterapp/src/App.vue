<script setup>
import { RouterView } from "vue-router";
import { onMounted } from "vue";
import API from "./API.js";

onMounted(() => {
  API.checkSessionStorage();
});
</script>

<template>
  <v-app>
      <v-app-bar class="bg-orange" title="Ditter"/>
      <v-main>
        <RouterView />
      </v-main>
  </v-app>
</template>