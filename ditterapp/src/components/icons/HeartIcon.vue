<script setup>
import { computed } from "vue";
import Heart from "../../assets/icons/heart.svg";
import HeartFilled from "../../assets/icons/heart-filled.svg";

const props = defineProps({ filled: Boolean });
const src = computed(() => {
  if (props.filled) {
    return HeartFilled;
  } else {
    return Heart;
  }
});
</script>

<template>
  <img :src="src" />
</template>
