<script setup lang="ts">
import Timeline from "../components/Timeline.vue";
import { provide, onMounted, ref } from "vue";
import API from "../API.js";

const timeline = ref([]);
provide("timeline", timeline);

onMounted(async () => {
  timeline.value = await API.getTimeline();
});
</script>

<template>
  <Timeline :dweets="timeline" class="bg-blue" />
</template>
