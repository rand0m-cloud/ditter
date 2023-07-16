<script setup>
import { ref, inject } from "vue";
import router from "../router";
import API from "../API.js";

const username = ref("");
const password = ref("");
const error = ref(null);

const submit = (e) => {
API.login(username.value, password.value);
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
        <input class="username-field" type="username" required v-model="username" />
        <label for="password-field">Password:</label>
        <input class="password-field" type="password" required v-model="password" />
        <button>Login</button>
      </form>
    </div>
  </div>
</template>

<style>
.login-container {
  display: flex;
  justify-content: center;
  padding-top: 1rem;
}

.login-form {
  display: flex;
  flex-direction: column;
  min-width: 40vw;
  max-width: 50vw;
  padding: 3rem;
  background-color: rgb(100, 100, 100, 0.2);
  border-radius: 0.5rem;
}

.login-form button,
.login-form input {
  width: 100%;
  margin-bottom: 0.5rem;
}

.login-form button {
  height: 2.5rem;
}

.login-error {
  margin-bottom: 1rem;
  background-color: rgba(255, 0, 0, 0.2);
  border-radius: 1rem;
  padding: 0.5rem;
}
</style>
