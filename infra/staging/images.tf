resource "docker_image" "django_staging" {
  name = "django_staging_server"

  build {
    context    = "../.."
    dockerfile = "infra/units/django_staging_server.dockerfile"
    label      = { project : "ditter" }
  }
}

resource "docker_image" "vue_staging" {
  name = "vue_prod"

  build {
    context    = "../.."
    dockerfile = "infra/units/vue_prod_server.dockerfile"
    label      = { project : "ditter" }
  }
}