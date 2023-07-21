<script setup>
import { ref, inject } from "vue";
import router from "../router";
import API from "../API.js";
import InputField from "../components/InputField.vue";

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
        <InputField>
          <label for="username-field">Username:</label>
          <input
            autocomplete="username"
            class="username-field"
            type="text"
            required
            v-model="username"
          />
        </InputField>
        <InputField>
          <label for="password-field">Password:</label>
          <input
            autocomplete="password"
            class="password-field"
            type="password"
            required
            v-model="password"
          />
        </InputField>
        <InputField>
          <button>Login</button>
        </InputField>
      </form>
    </div>
  </div>
</template>

<style>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: fit-content;
}

.login-form {
  display: flex;
  flex-direction: column;
  width: 90vw;
  max-width: 50rem;
  padding: 3rem;
  background-color: var(--primary-color);
  border-radius: 2rem;
}

.login-error {
  margin-bottom: 1rem;
  background-color: var(--error-color);
  color: var(--error-text-color);
  border-radius: 1rem;
  padding: 1rem;
}
</style>
