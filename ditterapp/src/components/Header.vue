<script setup>
import { computed, inject } from "vue";
import { RouterLink } from "vue-router";
import API from "../API.js";

const username = computed(() => {
  if (!API.user.value) {
    return "Not Logged In";
  } else {
    return API.user.value.author_display_name;
  }
});
</script>

<template>
  <header>
    <RouterLink to="/">
      <h1 class="header-name">Ditter</h1>
    </RouterLink>
    <RouterLink to="/login">
      <h2 class="header-profile">{{ username }}</h2>
    </RouterLink>
  </header>
</template>

<style>
header {
  background-color: var(--primary-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
}

.header-name {
  color: var(--logo-text-color);
}

.header-profile {
  color: var(--primary-text-color);
}
</style>
