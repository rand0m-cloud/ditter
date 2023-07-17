<script setup>
import { ref, inject } from "vue";
import router from "../router";
import API from "../API.js";

const username = ref("");
const password = ref("");
const error = ref(null);

const submit = (e) => {
  API.login(username.value, password.value).then((resp) => {
    if (resp["error"]) {
      error.value = resp["error"];
    }
  });
  e.preventDefault();
  return false;
};
</script>

<template>
  <div class="login-container">
    <div class="login-form">
      <p v-if="error" class="login-error">{{ error }}</p>
      <form @submit="submit">
        <label for="username-field">Username:</label>
        <input
          autocomplete="username"
          class="username-field"
          type="text"
          required
          v-model="username"
        />
        <label for="password-field">Password:</label>
        <input
          autocomplete="password"
          class="password-field"
          type="password"
          required
          v-model="password"
        />
        <button>Login</button>
      </form>
    </div>
  </div>
</template>

<style>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 1rem;
  max-height: 25rem;
}

.login-form {
  display: flex;
  flex-direction: column;
  min-width: 40vw;
  max-width: 50vw;
  padding: 3rem;
  background-color: var(--primary-color);
  border-radius: 0.5rem;
}

.login-form button,
.login-form input {
  width: 100%;
  margin-bottom: 0.5rem;
}

.login-form button {
  height: 2.5rem;
  background-color: var(--active-color);
  color: var(--active-text-color);
  border: none;
  border-radius: 2rem;
}

.login-error {
  margin-bottom: 1rem;
  background-color: var(--error-color);
  color: var(--error-text-color);
  border-radius: 1rem;
  padding: 1rem;
}

.login-form label {
  padding: 0.5rem 0;
  display: block;
  color: var(--active-text-color);
}
</style>
