resource "docker_image" "django_prod" {
  name = "django_prod_server"

  build {
    context    = "../.."
    dockerfile = "infra/units/django_prod_server.dockerfile"
    label      = { project : "ditter" }
  }
}

resource "docker_image" "vue_prod" {
  name = "vue_prod"

  build {
    context    = "../.."
    dockerfile = "infra/units/vue_prod_server.dockerfile"
    label      = { project : "ditter" }
  }
}

resource "docker_image" "postgres_prod" {
  name = "postgres:15.3"
}