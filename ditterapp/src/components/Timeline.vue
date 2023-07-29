<script setup>
import Dweet from "./Dweet.vue";

const props = defineProps({ dweets: Array });
</script>

<template>
  <div class="timeline">
    <v-container fluid>
      <v-row justify="space-around">
        <v-col xl="4" md="6" sm="8">
          <Dweet v-for="dweet in props.dweets" :key="dweet.uuid" :dweet="dweet" />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
