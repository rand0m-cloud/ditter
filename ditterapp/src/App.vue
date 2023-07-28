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
  <v-layout>
  <v-app-bar class="bg-orange"> 
    <v-app-bar-title class="text-h5 text-blue-darken-4">Ditter</v-app-bar-title>
  </v-app-bar>
  <v-main>
    <RouterView />
    </v-main>
  </v-layout>
  </v-app>
</template>
