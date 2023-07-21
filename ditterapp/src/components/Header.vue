<script setup>
import { computed } from "vue";
import { RouterLink } from "vue-router";
import API from "../API.js";

const logged_in = computed(() => {
  return !!API.user.value;
});

const user_link = computed(() => {
  if (!logged_in.value) {
    return null;
  } else {
    return `/user/${API.user.value.author_username}`;
  }
});
</script>

<template>
  <header>
    <RouterLink to="/">
      <h1 class="header-name">Ditter</h1>
    </RouterLink>
    <RouterLink :to="user_link" v-if="logged_in">
      <h3 class="header-profile">{{ API.user.value.author_username }}</h3>
    </RouterLink>
    <RouterLink to="/login" v-if="!logged_in">
      <h3 class="header-profile">Log In</h3>
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

  position: sticky;
  top: 0rem;
}

.header-name {
  color: var(--logo-text-color);
  font-size: xx-large;
}

.header-profile {
  color: var(--primary-text-color);
}
</style>
