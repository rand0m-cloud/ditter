<template>
  <div class="register-view">
    <h1>Register</h1>
    <form>
      <label for="display-name-field">Display Name:</label>
      <input class="display-name-field" type="text" required />
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
        autocomplete="new-password"
        class="password-field"
        type="password"
        required
        v-model="password"
      />
      <label for="password-field">Confirm Password:</label>
      <input class="password-field" type="password" required v-model="password" />
      <label for="invite-code-field">Invite Code:</label>
      <input class="invite-code-field" type="text" required />
      <button>Register</button>
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
  width: 25rem;
  height: fit-content;

  display: flex;
  flex-direction: column;
}

.register-view > form {
  display: flex;
  flex-direction: column;
}

.register-view button {
  background-color: var(--active-color);
  color: var(--active-text-color);
  border: none;
  border-radius: 2rem;
  margin-top: 1rem;
  height: 3rem;
}

.register-view input {
  margin-top: 0.5rem;
  background-color: var(--secondary-color);
  color: var(--secondary-text-color);
  border: 2px solid var(--active-color);
  border-radius: 1rem;
  padding: 0.5rem;
}

.register-view label {
  margin-top: 0.5rem;
}
</style>
