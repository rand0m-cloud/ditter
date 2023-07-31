<script setup>
import Dweet from "./Dweet.vue";

const props = defineProps({ dweets: Array });
</script>

<template>
  <div class="timeline h-100">
    <v-container>
      <v-row justify="space-around">
        <v-col xs="12" sm="8" md="6" lg="4" xl="3">
          <Dweet v-for="dweet in props.dweets" :key="dweet.uuid" :dweet="dweet" />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
