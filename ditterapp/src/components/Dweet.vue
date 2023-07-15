<script setup>
import { inject } from 'vue'
import HeartIcon from '../components/icons/HeartIcon.vue'

const props = defineProps({ dweet: Object })
const api_backend = inject('api_backend')
const user = inject('user')

const like = () => {
  console.log(api_backend)
  fetch(`${api_backend}/api/v1/like/${props.dweet.uuid}`, {
    method: 'POST',
    body: JSON.stringify({ session: user.value.session })
  })
}
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
        ><button alt="Like this Dweet" @click="like"><HeartIcon /></button>
      </div>
    </div>
  </div>
</template>

<style>
.dweet {
  padding: 1rem;
  margin: 0.5rem;
  border: solid 0.25rem;
  height: 10rem;
  border-radius: 1rem;

  display: flex;
  justify-content: space-between;
  flex-direction: column;
}

.dweet-content {
  flex-grow: 1;
}

.dweet-author {
  padding: 0.5rem 0;
}

.dweet-author > .display-name {
  font-weight: 550;
}

.dweet-author > .username {
  color: gray;
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
