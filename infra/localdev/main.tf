terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_container" "django_dev" {
  name  = "django_dev"
  image = docker_image.django_dev.image_id

  ports {
    internal = 8000
    external = var.backend_port
  }

  user =  var.run_as_uid

  volumes {
    container_path = "/app"
    host_path      = "${path.cwd}/../.."
  }

}

resource "docker_container" "vue_dev" {
  name  = "vue_dev"
  image = docker_image.vue_dev.image_id

  ports {
    internal = 3000
    external = var.frontend_port
  }

  user =  var.run_as_uid

  env = ["PORT=${var.frontend_port}"]

  volumes {
    container_path = "/app"
    host_path      = "${path.cwd}/../../ditterapp"
  }

}