terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_network" "ditter_network" {
  name = "ditter_network"
}

resource "docker_container" "django_prod" {
  name  = "django_prod"
  image = docker_image.django_prod.image_id

  ports {
    internal = 80
    external = var.backend_port
  }

  networks_advanced {
    name = docker_network.ditter_network.name
  }

  depends_on = [docker_container.postgres_prod]

  volumes {
    container_path = "/etc/nginx/nginx.conf"
    host_path      = "${path.cwd}/../units/django_nginx.conf"
  }
}

resource "docker_container" "vue_prod" {
  name  = "vue_prod"
  image = docker_image.vue_prod.image_id

  ports {
    internal = 80
    external = var.frontend_port
  }

  volumes {
    container_path = "/etc/nginx/nginx.conf"
    host_path      = "${path.cwd}/../units/vue_nginx.conf"
  }
}

resource "docker_container" "postgres_prod" {
  name     = "postgres_prod"
  hostname = "ditterdb"
  image    = docker_image.postgres_prod.image_id

  env = ["POSTGRES_PASSWORD=${var.db_password}", "POSTGRES_USER=${var.db_username}", "POSTGRES_DB=${var.db_name}", "PGDATA=/var/lib/postgresql/data/pgdata"]

  networks_advanced {
    name = docker_network.ditter_network.name
  }
  volumes {
    container_path = "/var/lib/postgresql/data"
    host_path      = var.db_storage_path
  }
}