<script setup>
import { computed } from "vue";
import API from "../API.js";

const props = defineProps({ dweet: Object });
const has_liked = computed(() => {
  return props.dweet.liked_by.includes(API.user.value?.author_username);
});

const like = () => {
  if (API.user.value && !props.dweet.liked_by.includes(API.user.value.author_username)) {
    API.likeDweet(props.dweet.uuid);
    props.dweet.liked_by.push(API.user.value.author_username);
    props.dweet.likes += 1;
  }
};
</script>

<template>
  <v-card class="mb-3 pa-2" elevation="8">
    <v-card-title class="dweet-author">{{ props.dweet.author_display_name }}</v-card-title>
    <v-card-subtitle>{{ props.dweet.author_username }}</v-card-subtitle>
    <v-card-text>{{ props.dweet.content }}</v-card-text>
    <v-card-actions>
      <v-btn density="compact" rounded size="medium" class="pa-1" @click="like">
        <span class="pr-1 text-caption">{{ props.dweet.likes }}</span>
        <v-icon>
          {{ has_liked ? "mdi-heart" : "mdi-heart-outline" }}
        </v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<style>
.v-card-title.dweet-author {
padding-bottom:0;
}
</style>