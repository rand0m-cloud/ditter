terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_container" "django_staging" {
  name  = "django_staging"
  image = docker_image.django_staging.image_id

  ports {
    internal = 80
    external = var.backend_port
  }

  volumes {
    container_path = "/etc/nginx/nginx.conf"
    host_path      = "${path.cwd}/../units/django_nginx.conf"
  }
}

resource "docker_container" "vue_staging" {
  name  = "vue_staging"
  image = docker_image.vue_staging.image_id

  ports {
    internal = 80
    external = var.frontend_port
  }

  volumes {
    container_path = "/etc/nginx/nginx.conf"
    host_path      = "${path.cwd}/../units/vue_nginx.conf"
  }
}