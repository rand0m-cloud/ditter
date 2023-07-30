<script setup>
import { ref } from "vue";
import API from "../API.js";
import router from "../router";

const display_name = ref("");
const username = ref("");
const password = ref("");
const password_confirm = ref("");
const invite_code = ref("");
const errors = ref([]);

const fields = [
  [display_name, "Display Name"],
  [username, "Username"],
  [password, "Password"],
];

const submit = async (e) => {
  e.preventDefault();
  const form_errors = [];
  if (password.value != password_confirm.value) {
    form_errors.push("Passwords do not match");
  }

  if (display_name.value == "") {
    form_errors.push("Display Name cannot be empty");
  }

  if (username.value == "") {
    form_errors.push("Username cannot be empty");
  }

  if (password.value == "") {
    form_errors.push("Password cannot be empty");
  }

  if (invite_code.value == "") {
    form_errors.push("Invite Code cannot be empty");
  }

  if (form_errors.length > 0) {
    errors.value = form_errors;
    return;
  }

  let resp = await API.register({
    username: username.value,
    password: password.value,
    invite_code: invite_code.value,
    display_name: display_name.value,
  });

  if (resp["error"]) {
    errors.value = [];
    errors.value.push(...resp["error"]);
  } else {
    await API.login(username.value, password.value);
    router.push("/");
  }
};
</script>

<template>
  <div class="bg-blue h-100">
    <v-container>
      <v-row justify="space-around">
        <v-col sm="10" md="8" lg="6">
          <v-sheet elevation="8" class="pa-4" rounded="xl">
            <v-form @submit.prevent>
              <v-container>
                <v-row>
                  <v-col>
                    <p class="text-h5">Register</p>
                  </v-col>
                </v-row>
                <v-row v-for="error in errors" v-if="errors.length > 0">
                  <v-col>
                    <v-alert :text="error" class="bg-error" />
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <v-text-field v-model="display_name" label="Display Name" />
                    <v-text-field v-model="username" label="Username" autocomplete="username" />
                    <v-text-field v-model="password" label="Password" type="password" />
                    <v-text-field
                      v-model="password_confirm"
                      label="Confirm Password"
                      autocomplete="new-password"
                      type="password"
                    />
                    <v-text-field v-model="invite_code" label="Invite Code" />
                  </v-col>
                </v-row>
                <v-row justify="space-around">
                  <v-col sm="8" md="6">
                    <v-btn block @click="submit">Register</v-btn>
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
