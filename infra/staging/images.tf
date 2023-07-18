resource "docker_image" "django_staging" {
  name = "django_staging"

  build {
    context    = "../.."
    dockerfile = "infra/units/django_prod_server.dockerfile"
    label      = { project : "ditter" }
  }
}
resource "docker_image" "vue_staging" {
  name = "vue_staging"

  build {
    context    = "../.."
    dockerfile = "infra/units/vue_prod_server.dockerfile"
    label      = { project : "ditter" }
  }
}


resource "docker_image" "postgres_staging" {
  name = "postgres:15.3"
}