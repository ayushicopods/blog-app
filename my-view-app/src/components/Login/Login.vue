<template>
  <div class="registration-card">
    <!-- image -->
    <div>
      <img src="/registration.svg" alt="registration" />
    </div>
    <!-- registration form -->
    <div class="registration-card-right">
      <div>
        <p>Login</p>
        <p>
          the ability to create and manage blog posts, follow other bloggers,
          and engage with the community
        </p>
      </div>
      <div>
        <div class="custom-input">
          <label for="name"> User Name </label>
          <div>
            <input
              v-model="userName"
              placeholder="Enter UserName"
              class="border-0 focus:outline-none w-full"
            />
          </div>
        </div>
        <!-- Enter password  -->
        <div class="custom-input">
          <label for="name"> Password </label>
          <div>
            <input v-model="password" placeholder="Enter Password" />
          </div>
        </div>
      </div>
      <!-- Register button -->
      <div>
        <button @click="reset">Clear</button>
        <button @click="login">Submit</button>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const userName = ref("");
const password = ref("");

const router = useRouter();
onMounted(() => {
  const userData = localStorage.getItem("userData");
  if (userData) router.push("/");
});

function login() {
  const config = {
    method: "post",
    maxBodyLength: Infinity,
    url: "http://127.0.0.1:8000/api/token/",
    headers: {
      "Content-Type": "application/json",
    },
    data: JSON.stringify({
      username: userName.value,
      password: password.value,
    }),
  };

  axios.request(config).then((response) => {
    if (response.status === 200) {
      console.log({ response });
      const userData = {
        accessToken: response.data.access,
        refreshToken: response.data.refresh,
      };
      localStorage.setItem("userData", JSON.stringify(userData));
      const storedData = JSON.parse(localStorage.getItem("userData"));
      console.log(storedData);
    }
  });
}
</script>
<style scoped src="./Login.css"></style>
