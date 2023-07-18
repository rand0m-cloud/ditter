
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  registry_auth {
    address     = "us-central1-docker.pkg.dev"
    config_file = pathexpand("~/.docker/config.json")
  }
}


resource "docker_registry_image" "django_prod" {
  name = "us-central1-docker.pkg.dev/ditter/ditterrepo/django:latest"
  keep_remotely = true
  triggers = {hash =  docker_image.django_prod.repo_digest}
}

resource "docker_registry_image" "vue_prod" {
  name = "us-central1-docker.pkg.dev/ditter/ditterrepo/vue:latest"
  keep_remotely = true
  triggers = {hash =  docker_image.vue_prod.repo_digest}
}

resource "docker_image" "django_prod" {
  name = "us-central1-docker.pkg.dev/ditter/ditterrepo/django:latest"

  build {
    context    = "../.."
    dockerfile = "infra/units/django_prod_server.dockerfile"
    label      = { project : "ditter" }
  }
}
resource "docker_image" "vue_prod" {
  name = "us-central1-docker.pkg.dev/ditter/ditterrepo/vue:latest"

  build {
    context    = "../.."
    dockerfile = "infra/units/vue_prod_server.dockerfile"
    label      = { project : "ditter" }

}
}