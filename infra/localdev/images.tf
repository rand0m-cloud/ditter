resource "docker_image" "django_dev" {
  name = "django_dev_server"

  build {
    context    = "../.."
    dockerfile = "infra/units/django_dev_server.dockerfile"
    label      = { project : "ditter" }
  }
}

resource "docker_image" "vue_dev" {
  name = "vue_dev"

  build {
    context    = "../.."
    dockerfile = "infra/units/vue_dev_server.dockerfile"
    label      = { project : "ditter" }
  }
}