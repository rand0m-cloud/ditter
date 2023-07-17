<script setup>
const props = defineProps({ open: Boolean, on_clickaway: Function });
</script>

<template>
  <template v-if="props.open">
    <div class="modal-back" @click="props.on_clickaway"></div>
    <div class="modal-content"><slot /></div>
  </template>
</template>

<style>
.modal-back {
  position: absolute;
  width: 100vw;
  height: 100vh;
  background-color: var(--modal-back-color);
  opacity: 50%;
  top: 0;
}

.modal-content {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  top: 0;
  height: 100%;
  width: 100%;
  pointer-events: none;
}

.modal-content > * {
  pointer-events: auto;
}
</style>
