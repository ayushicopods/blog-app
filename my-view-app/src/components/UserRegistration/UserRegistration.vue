<template>
  <div class="registration-card">
    <!-- image -->
    <div>
      <img src="/registration.svg" alt="registration" />
    </div>
    <!-- registration form -->
    <div class="registration-card-right">
      <div>
        <p>Registration</p>
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
        <div class="custom-input">
          <label for="name"> Email </label>
          <div>
            <input v-model="email" placeholder="Enter Email" />
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
        <button @click="register">Submit</button>
      </div>
    </div>
  </div>
</template>
<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const userName = ref("");
const password = ref("");
const email = ref("");

const router = useRouter();
onMounted(() => {
  const userData = localStorage.getItem("userData");
  if (userData) router.push("/");
});

function reset() {
  userName.value = "";
  password.value = "";
  email.value = "";
}

function register() {
  let config = {
    method: "post",
    maxBodyLength: Infinity,
    url: "http://127.0.0.1:8000/api/register/",
    headers: {
      "Content-Type": "application/json",
    },
    data: JSON.stringify({
      username: userName.value,
      email: email.value,
      password: password.value,
    }),
  };

  axios
    .request(config)
    .then((response) => {
      if (response.status === 201) {
        router.push("/login");
      }
    })
    .catch((error) => {
      console.log(error);
    });
}
</script>
<style scoped src="./UserRegistration.css"></style>
