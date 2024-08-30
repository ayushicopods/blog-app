<template>
  <div>Hello</div>
</template>
<script setup>
import { onMounted } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
onMounted(() => {
  const userData = localStorage.getItem("userData");
  if (!userData) router.push("/register");
});
</script>
