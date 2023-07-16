<script setup lang="ts">
import Dweet from "../components/Dweet.vue";
import ComposeDweetModal from "../components/ComposeDweetModal.vue";
import { provide, onMounted, ref } from "vue";
import router from "../router";
import API from "../API.js";

const timeline = ref([]);
provide("timeline", timeline);

onMounted(async () => {
  timeline.value = await API.getTimeline();
});
</script>

<template>
  <main>
    <div class="timeline">
      <template v-for="dweet in timeline">
        <Dweet :dweet="dweet" />
      </template>
    </div>
    <ComposeDweetModal />
  </main>
</template>

<style>
.timeline {
  width: 50vw;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
