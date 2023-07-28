<script setup>
import { ref } from "vue";
import { RouterLink } from "vue-router";
import router from "../router";
import API from "../API.js";
const username = ref("");
const password = ref("");
const error = ref(null);

const submit = (e) => {
  API.login(username.value, password.value).then((resp) => {
    if (resp["error"]) {
      error.value = resp["error"];
    } else {
      router.push("/");
    }
  });
  e.preventDefault();
  return false;
};
</script>

<template></template>
