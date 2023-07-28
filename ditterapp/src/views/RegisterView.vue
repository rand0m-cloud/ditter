<script setup>
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

<template></template>
