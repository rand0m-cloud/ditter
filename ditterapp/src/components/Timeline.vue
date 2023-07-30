<script setup>
import Dweet from "./Dweet.vue";

const props = defineProps({ dweets: Array });
</script>

<template>
  <div class="timeline">
    <v-container fluid>
      <v-row justify="space-around">
        <v-col cols="8" xl="4">
          <Dweet v-for="dweet in props.dweets" :key="dweet.uuid" :dweet="dweet" />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
