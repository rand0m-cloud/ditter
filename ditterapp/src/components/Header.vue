<script setup>
import { computed, inject } from "vue";
import { RouterLink } from "vue-router";

const user = inject("user");

const username = computed(() => {
  if (!user.value) {
    return "Not Logged In";
  } else {
    return user.value.author_display_name;
  }
});
</script>

<template>
  <header>
    <RouterLink to="/">
      <h1 class="header-name">Ditter</h1>
    </RouterLink>
    <RouterLink to="/login">
      <h2>{{ username }}</h2>
    </RouterLink>
  </header>
</template>

<style>
header {
  background-color: rgba(50, 50, 50, 0.3);
  display: flex;
  justify-content: space-between;
  padding: 1rem;
}
.header-name {
}
</style>
