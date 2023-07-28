<script setup>
import Dweet from "./Dweet.vue";

const props = defineProps({ dweets: Array });
</script>

<template>
  <v-container fluid class="h-100">
    <v-row justify="space-around">
      <v-col xl="4" md="6" sm="8">
        <Dweet v-for="dweet in props.dweets" :key="dweet.uuid" :dweet="dweet" />
      </v-col>
    </v-row>
  </v-container>
</template>
