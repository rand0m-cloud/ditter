<script setup>
import { ref } from "vue";
import { RouterLink } from "vue-router";
import router from "../router";
import API from "../API.js";
const username = ref("");
const password = ref("");
const error = ref(null);

const submit = (e) => {
  API.login(username.value, password.value).then((resp) => {
    if (resp["error"]) {
      error.value = resp["error"];
    } else {
      router.push("/");
    }
  });
  e.preventDefault();
  return false;
};
</script>

<template>
  <div class="bg-blue h-100">
    <v-container fluid>
      <v-row justify="space-around">
        <v-col xs="12" sm="10" md="8" lg="6" xl="4">
          <v-sheet rounded class="pa-2" elevation="8">
            <v-form @submit.prevent>
              <v-container fluid>
                <v-row v-if="error">
                  <v-col>
                    <v-alert :text="error" class="bg-error" />
                  </v-col>
                </v-row>
                <v-row justify="space-around">
                  <v-col>
                    <v-text-field v-model="username" label="Username" autocomplete="username" />
                    <v-text-field
                      v-model="password"
                      label="Password"
                      type="password"
                      autocomplete="password"
                    />
                  </v-col>
                </v-row>
                <v-row justify="space-around">
                  <v-col sm="6" md="6">
                    <v-btn block type="submit" @click="submit">Login</v-btn>
                  </v-col>
                </v-row>
                <v-row justify="space-around">
                  <v-col sm="6" md="6">
                    <p class="text-center">
                      Need an account?
                      <RouterLink to="/register"><span>Create one</span></RouterLink>
                    </p>
                  </v-col>
                </v-row>
              </v-container>
            </v-form>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
