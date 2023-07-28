<script setup>
import { onMounted, ref, computed, watch } from "vue";
import { useRoute } from "vue-router";
import router from "../router";
import API from "../API.js";

const route = useRoute();
const data = ref(null);
const error = ref(null);

const fetch_data = async () => {
  let resp = await API.getUser(route.params.username);
  if (resp["error"]) {
    error.value = resp["error"];
  } else {
    data.value = resp;
  }
};

onMounted(fetch_data);
watch(route, fetch_data);

const is_users_profile = computed(() => {
  return API.getLoggedInUser()?.author_username == route.params.username;
});

const logout = async () => {
  await API.logout();
  router.push("/");
};
</script>

<template></template>
