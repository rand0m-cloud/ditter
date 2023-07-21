<script setup lang="ts">
import Dweet from "../components/Dweet.vue";
import ComposeDweetModal from "../components/ComposeDweetModal.vue";
import { provide, onMounted, ref } from "vue";
import API from "../API.js";

const timeline = ref([]);
provide("timeline", timeline);

onMounted(async () => {
  timeline.value = await API.getTimeline();
});
</script>

<template>
  <div class="timeline">
    <template v-for="dweet in timeline">
      <Dweet :dweet="dweet" />
    </template>
  </div>
  <ComposeDweetModal />
</template>

<style>
.timeline {
  width: 90vw;
  max-width: 50rem;

  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: 2rem 2rem 0 0;
}
</style>
