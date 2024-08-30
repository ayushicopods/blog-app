<template>
  <div class="border border-gray1 p-2 rounded">
    <input
      v-model="inputValue"
      :placeholder="placeholder"
      class="border-0 focus:outline-none w-full"
      @change="emit('updateValue', inputValue)"
    />
  </div>
</template>
<script setup>
import { defineProps, ref, defineEmits } from "vue";

const props = defineProps({
  placeholder: {
    type: String,
    default: "",
  },
  modelValue: {
    type: String,
    default: "",
  },
});

const inputValue = ref(props.modelValue);
console.log("hello");
const emit = defineEmits(["updateValue"]);
</script>
