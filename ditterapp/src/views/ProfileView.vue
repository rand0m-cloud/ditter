<script setup>
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import Dweet from "../components/Dweet.vue";
import API from "../API.js";

const route = useRoute();
const data = ref(null);
const error = ref(null);

onMounted(async () => {
  let resp = await API.getUser(route.params.username);
  if (resp["error"]) {
    error.value = resp["error"];
  } else {
    data.value = resp;
  }
});
</script>

<template>
  <div class="profile">
    <div v-if="error" class="profile-error">
      {{ error }}
    </div>
    <div v-if="data" class="profile-view">
      <div class="profile-header">
        <h2>{{ data.author.author_display_name }}</h2>
        <h3>@{{ data.author.author_username }}</h3>
      </div>
      <div class="profile-timeline">
        <Dweet v-for="dweet in data.dweets" :dweet="dweet" />
      </div>
    </div>
  </div>
</template>

<style>
.profile {
  background-color: var(--secondary-color);
  border-radius: 1rem;
  padding: 1rem;
  margin: 1rem 0;
  width: 100%;
  max-width: 30rem;

  display: flex;
  align-items: center;
  flex-direction: column;
}

.profile-view {
  width: 100%;
}

.profile-header {
  margin-bottom: 2rem;
}

.profile-timeline {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.profile-error {
  color: var(--secondary-text-color);
}
</style>
