<script setup>
import { inject, ref } from "vue";
import Modal from "./Modal.vue";
import API from "../API.js";

const is_compose_modal_open = ref(false);
const dweet_content = ref("");
const timeline = inject("timeline");

const open_compose_modal = () => {
  if (!API.user) {
    router.push("/login");
    return;
  }
  is_compose_modal_open.value = true;
};

const close_compose_modal = () => {
  is_compose_modal_open.value = false;
};

const post = async () => {
  if (dweet_content.value == "") {
    return;
  }
  close_compose_modal();
  let resp = await API.postDweet(dweet_content.value);
  if (resp["error"]) {
    return;
  }

  let uuid = resp["uuid"];

  let dweet = await API.getDweet(uuid);
  timeline.value.unshift(dweet);
};
</script>

<template>
  <button class="create-dweet-fab" @click="open_compose_modal">
    <h3>Compose Dweet</h3>
  </button>
  <Modal :open="is_compose_modal_open" :on_clickaway="close_compose_modal">
    <div class="compose-modal">
      <textarea type="text" v-model="dweet_content" placeholder="What is on your mind?" />
      <button @click="post">Post</button>
    </div>
  </Modal>
</template>

<style>
.create-dweet-fab {
  position: fixed;
  right: 2rem;
  bottom: 2rem;
  background-color: var(--active-color);
  padding: 1rem;
  border-radius: 2rem;
  color: var(--active-text-color);
  border: none;
}

.compose-modal {
  width: 70vw;
  max-width: 40rem;
  min-height: 20rem;
  border-radius: 1rem;
  padding: 2rem;

  display: flex;
  flex-direction: column;

  background-color: var(--modal-front-color);
}

.compose-modal textarea {
  width: 100%;
  flex-grow: 10;
  resize: none;
  font-family: inherit;
  background-color: var(--primary-color);
  color: var(--primary-text-color);
  border: none;
  border-radius: 2rem;
  padding: 2rem;
}

.compose-modal button {
  margin: 1rem 3rem 0 3rem;
  flex-grow: 1;
  background-color: var(--active-color);
  border: none;

  color: var(--active-text-color);
  font-weight: bold;
  border-radius: 2rem;
}
</style>
