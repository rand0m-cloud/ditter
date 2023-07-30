<script setup lang="ts">
import Timeline from "../components/Timeline.vue";
import { provide, onMounted, ref, computed } from "vue";
import API from "../API.js";

const timeline = ref([]);
const is_compose_open = ref(false);
const dweet_content = ref("");
const success_snackbar_open = ref(false);
const error = ref(null);

onMounted(async () => {
  timeline.value = await API.getTimeline();
});

const logged_in = computed(() => {
  return !!API.user.value;
});

const send_dweet = async () => {
  let resp = await API.postDweet(dweet_content.value);
  if (resp.error) {
    error.value = resp["error"];
    return;
  }

  timeline.value.unshift(await API.getDweet(resp.uuid));

  is_compose_open.value = false;
  success_snackbar_open.value = true;
  error.value = null;
};
</script>

<template>
  <Timeline :dweets="timeline" class="bg-blue" />
  <v-btn
    v-if="logged_in"
    rounded
    class="fab bg-orange"
    @click="is_compose_open = true"
    position="fixed"
  >
    <v-icon>mdi-pencil-box</v-icon>
    Compose Dweet
  </v-btn>
  <v-dialog v-model="is_compose_open" width="auto">
    <v-card class="pa-8 bg-orange" rounded>
      <v-alert v-if="error" :text="error" color="error" />
      <v-container class="pa-8 h-40">
        <v-row>
          <v-col>
            <textarea
              class="pa-4 dweet-input"
              placeholder="Whats on your mind?"
              cols="40"
              rows="5"
              v-model="dweet_content"
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-btn class="mt-4" block @click="send_dweet"> <v-icon>mdi-send</v-icon>Send </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
  </v-dialog>
  <v-snackbar v-model="success_snackbar_open" timeout="2000">Dweet Sent!</v-snackbar>
</template>

<style>
.fab {
  bottom: 1rem;
  right: 1rem;
}

.dweet-input {
  border: 1px solid black;
  resize: none;
}
</style>
