<script setup>
import InputField from "../components/InputField.vue";
</script>

<template>
  <div class="register-view">
    <h1>Register</h1>
    <form class="register-form">
      <InputField>
        <label for="display-name-field">Display Name:</label>
        <input class="display-name-field" type="text" required />
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
        <input class="password-field" type="password" required v-model="password" />
      </InputField>
      <InputField>
        <label for="invite-code-field">Invite Code:</label>
        <input class="invite-code-field" type="text" required />
      </InputField>
      <InputField>
        <button>Register</button>
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

  width:100vw;
  max-width: 50rem;
  height: fit-content;

  display: flex;
  flex-direction: column;
}

.register-form {
  display: flex;
  flex-direction: column;
  margin-top:2rem;
}

</style>
