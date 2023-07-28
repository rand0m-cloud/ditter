<script setup>
const props = defineProps({ dweet: Object });
</script>

<template>
  <v-card class="pa-3 mb-4">
    <div class="pb-2">
      <p class="text-subtitle-1">{{ props.dweet.author_display_name }}</p>
      <p class="text-caption">{{ props.dweet.author_username }}</p>
    </div>
    <p class="py-2 text-body-1">{{ props.dweet.content }}</p>
  </v-card>
</template>
