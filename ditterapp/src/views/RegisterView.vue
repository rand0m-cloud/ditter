<script setup>
import InputField from "../components/InputField.vue";
import { ref } from "vue";
import API from "../API.js";
import router from "../router";

const display_name = ref("");
const username = ref("");
const password = ref("");
const password_confirm = ref("");
const invite_code = ref("");
const errors = ref([]);

const submit = async (e) => {
  e.preventDefault();
  const form_errors = [];
  if (password.value != password_confirm.value) {
    form_errors.push("Passwords do not match");
  }

  if (display_name.value == "") {
    form_errors.push("Display Name cannot be empty");
  }

  if (username.value == "") {
    form_errors.push("Username cannot be empty");
  }

  if (password.value == "") {
    form_errors.push("Password cannot be empty");
  }

  if (invite_code.value == "") {
    form_errors.push("Invite Code cannot be empty");
  }

  if (form_errors.length > 0) {
    errors.value = form_errors;
    return;
  }

  let resp = await API.register({
    username: username.value,
    password: password.value,
    invite_code: invite_code.value,
    display_name: display_name.value,
  });

  if (resp["error"]) {
    errors.value = [];
    errors.value.push(...resp["error"]);
  } else {
    await API.login(username.value, password.value);
    router.push("/");
  }
};
</script>

<template>
  <div class="register-view">
    <h1>Register</h1>
    <p v-for="error in errors" class="register-error">
      {{ error }}
    </p>
    <form class="register-form">
      <InputField>
        <label for="display-name-field">Display Name:</label>
        <input class="display-name-field" type="text" required v-model="display_name" />
      </InputField>
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
          autocomplete="new-password"
          class="password-field"
          type="password"
          required
          v-model="password"
        />
      </InputField>
      <InputField>
        <label for="password-field">Confirm Password:</label>
        <input class="password-field" type="password" required v-model="password_confirm" />
      </InputField>
      <InputField>
        <label for="invite-code-field">Invite Code:</label>
        <input class="invite-code-field" type="text" required v-model="invite_code" />
      </InputField>
      <InputField>
        <button @click="submit">Register</button>
      </InputField>
    </form>
  </div>
</template>

<style>
.register-view {
  background-color: var(--primary-color);
  color: var(--primary-text-color);

  border-radius: 2rem;
  padding: 2rem;
  margin-top: 2rem;

  width: 100vw;
  max-width: 50rem;
  height: fit-content;

  display: flex;
  flex-direction: column;
}

.register-form {
  display: flex;
  flex-direction: column;
  margin-top: 2rem;
}

.register-error {
  margin-top: 1rem;
  background-color: var(--error-color);
  color: var(--error-text-color);
  border-radius: 1rem;
  padding: 1rem;
}
</style>
