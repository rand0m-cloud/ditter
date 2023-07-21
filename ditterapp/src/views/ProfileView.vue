<script setup>
import { onMounted, ref, computed } from "vue";
import { useRoute } from "vue-router";
import router from "../router";
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

const is_users_profile = computed(() => {
  return API.getLoggedInUser()?.author_username == route.params.username;
});

const logout = async () => {
  await API.logout();
  router.push("/");
};
</script>

<template>
  <div class="profile">
    <div v-if="error" class="profile-error">
      {{ error }}
    </div>
    <div v-if="data" class="profile-view">
      <div class="profile-header">
        <div>
          <h2>{{ data.author.author_display_name }}</h2>
          <h3>@{{ data.author.author_username }}</h3>
        </div>
        <button class="profile-logout" @click="logout" v-if="is_users_profile">Log Out</button>
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
  display: flex;
  justify-content: space-between;
}

.profile-logout {
  color: var(--active-text-color);
  background-color: var(--active-color);
  border: none;
  border-radius: 1rem;
  padding: 0 2rem;
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
