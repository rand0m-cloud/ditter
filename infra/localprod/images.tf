resource "docker_image" "django_localprod" {
  name = "django_localprod_server"

  build {
    context    = "../.."
    dockerfile = "infra/units/django_prod_server.dockerfile"
    label      = { project : "ditter" }
  }
}

resource "docker_registry_image" "django_prod" {
  name = "us-central1-docker.pkg.dev/ditter/ditterrepo/django:latest"
  keep_remotely = true
  triggers = {hash =  docker_image.django_localprod.repo_digest}
}

resource "docker_tag" "django_prod" {
  source_image = docker_image.django_localprod.name
  target_image = "us-central1-docker.pkg.dev/ditter/ditterrepo/django:latest"
}

resource "docker_image" "vue_localprod" {
  name = "vue_localprod"

  build {
    context    = "../.."
    dockerfile = "infra/units/vue_prod_server.dockerfile"
    label      = { project : "ditter" }
  }
}

resource "docker_registry_image" "vue_prod" {
  name = "us-central1-docker.pkg.dev/ditter/ditterrepo/vue:latest"
  keep_remotely = true
  triggers = {hash =  docker_image.vue_localprod.repo_digest}
}

resource "docker_tag" "vue_prod" {
  source_image = docker_image.vue_localprod.name
  target_image = "us-central1-docker.pkg.dev/ditter/ditterrepo/vue:latest"
}

resource "docker_image" "postgres_localprod" {
  name = "postgres:15.3"
}