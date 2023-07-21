import router from "./router";
import { ref } from "vue";

class API {
  backend = ref(null);
  session = ref(null);
  user = ref(null);

  static new(backend) {
    let api = new API();
    api.backend.value = backend;
    return api;
  }

  checkSessionStorage() {
    const storedUser = sessionStorage.getItem("user");
    if (storedUser) {
      console.log(storedUser);
      this.user.value = JSON.parse(storedUser);
    }
  }

  async likeDweet(uuid) {
    let resp = await fetch(`${this.backend.value}/api/v1/like/${uuid}`, {
      method: "POST",
      body: JSON.stringify({ session: this.user.value.session }),
    });
    resp = await resp.json();

    return resp;
  }

  async postDweet(content) {
    let resp = await fetch(`${this.backend.value}/api/v1/dweet`, {
      method: "POST",
      body: JSON.stringify({ session: this.user.value.session, content }),
    });
    resp = await resp.json();
    return resp;
  }

  async getTimeline() {
    let resp = await fetch(`${this.backend.value}/api/v1/timeline`);
    return await resp.json();
  }

  async getDweet(uuid) {
    let resp = await fetch(`${this.backend.value}/api/v1/dweet/${uuid}`);
    return await resp.json();
  }

  async login(username, password) {
    const resp = await fetch(`${this.backend.value}/api/v1/login`, {
      method: "POST",
      body: JSON.stringify({ username, password }),
    });

    const json = await resp.json();
    if (json["error"]) {
      return json;
    } else {
      this.user.value = json;
      sessionStorage.setItem("user", JSON.stringify(json));
      router.push("/");

      return {};
    }
  }

  async getUser(username) {
    let resp = await fetch(`${this.backend.value}/api/v1/user/${username}`);
    return await resp.json();
  }

  async register({ username, password, invite_code, display_name }) {
    const resp = await fetch(`${this.backend.value}/api/v1/register`, {
      method: "POST",
      body: JSON.stringify({ username, password, invite_code, display_name }),
    });
    return await resp.json();
  }

  async logout() {
    const resp = await fetch(`${this.backend.value}/api/v1/logout`, {
      method: "POST",
      body: JSON.stringify({ session: this.user.value.session }),
    });
    this.user.value = null;
  }

  getLoggedInUser() {
    return this.user.value;
  }
}

export default API = API.new(`${location.protocol}//${location.hostname}:8000`);
