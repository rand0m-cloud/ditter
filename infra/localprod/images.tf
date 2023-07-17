resource "docker_image" "django_localprod" {
  name = "django_localprod_server"

  build {
    context    = "../.."
    dockerfile = "infra/units/django_prod_server.dockerfile"
    label      = { project : "ditter" }
  }
}

resource "docker_image" "vue_localprod" {
  name = "vue_localprod"

  build {
    context    = "../.."
    dockerfile = "infra/units/vue_prod_server.dockerfile"
    label      = { project : "ditter" }
  }
}

resource "docker_image" "postgres_localprod" {
  name = "postgres:15.3"
}