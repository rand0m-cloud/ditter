<template>
  <div class="input-field">
    <slot />
  </div>
</template>

<style>
.input-field button,
.input-field input {
  width: 100%;
  margin-bottom: 0.5rem;
  color: var(--secondary-text-color);
  background-color: var(--secondary-color);
  border: 1px solid var(--active-color);
  border-radius: 1rem;
  padding: 0.75rem;
  font-size: large;
}

.input-field button {
  background-color: var(--active-color);
  color: var(--active-text-color);
  border: none;
  border-radius: 2rem;
  margin-top: 1rem;
}

.input-field label {
  padding: 0.5rem 0;
  display: block;
  color: var(--primary-text-color);
  font-size: large;
}
</style>
