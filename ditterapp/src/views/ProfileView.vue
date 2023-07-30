<script setup>
import { onMounted, ref, computed, watch } from "vue";
import { useRoute } from "vue-router";
import router from "../router";
import API from "../API.js";
import Timeline from "../components/Timeline.vue";

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
</script>

<template>
  <div class="bg-blue h-100">
    <v-container>
      <v-row justify="space-around">
        <v-col cols="8">
          <v-sheet rounded class="pa-4 px-8" elevation="8">
            <p>{{ data?.author.author_display_name ?? "" }}</p>
            <p>@{{ route.params.username }}</p>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
    <Timeline :dweets="data?.dweets ?? []" />
  </div>
</template>
