<script setup>
import { inject, computed } from "vue";
import HeartIcon from "../components/icons/HeartIcon.vue";
import API from "../API.js";

const props = defineProps({ dweet: Object });

const like = async () => {
  let resp = await API.likeDweet(props.dweet.uuid);
  if (!resp["error"]) {
    props.dweet.liked_by.push(API.user.value.author_username);
    props.dweet.likes += 1;
  }
};
const liked = computed(() => {
  return props.dweet.liked_by.includes(API.user.value?.author_username ?? "");
});
</script>

<template>
  <div class="dweet">
    <div class="dweet-author">
      <div class="display-name">{{ props.dweet.author_display_name }}</div>
      <div class="username">@{{ props.dweet.author_username }}</div>
    </div>
    <div class="dweet-content">{{ props.dweet.content }}</div>
    <div class="dweet-widgets">
      <div class="like-widget">
        <span>{{ props.dweet.likes }}</span
        ><button alt="Like this Dweet" @click="like"><HeartIcon :filled="liked" /></button>
      </div>
    </div>
  </div>
</template>

<style>
.dweet {
  padding: 1rem;
  margin: 0.5rem 0;
  border: solid 0.25rem;
  min-height: 10rem;
  border-radius: 1rem;

  display: flex;
  justify-content: space-between;
  flex-direction: column;

  width: 100%;
  max-width: 40rem;
}

.dweet-content {
  flex-grow: 1;
  word-wrap: break-word;
}

.dweet-author {
  padding: 0.5rem 0 1rem 0;
}

.dweet-author > .display-name {
  font-weight: 550;
  color: var(--primary-text-color);
}

.dweet-author > .username {
  color: var(--secondary-text-color);
}

.dweet-widgets {
  padding: 1rem 0 0 0;
}

.like-widget {
  display: flex;
  align-items: center;
}

.like-widget > button > img {
  width: 2rem;
  height: 2rem;
}

.like-widget > button {
  background-color: unset;
  border: none;
}
</style>
