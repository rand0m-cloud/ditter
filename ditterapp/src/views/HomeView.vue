<script setup lang="ts">
import Dweet from '../components/Dweet.vue'
import { inject, onMounted, ref } from 'vue'

const data = ref([])

const api_backend = inject('api_backend')

onMounted(async () => {
  let resp = await fetch(`${api_backend}/api/v1/timeline`)
  data.value = await resp.json()
})
</script>

<template>
  <main>
    <div class="timeline">
      <template v-for="dweet in data">
        <Dweet :dweet="dweet" />
      </template>
    </div>
  </main>
</template>

<style>
.timeline {
  width: 50vw;
}
</style>
