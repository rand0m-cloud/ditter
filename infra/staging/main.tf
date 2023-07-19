terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
}

resource "docker_network" "ditter_network" {
  name = "ditter_network"
}

resource "docker_container" "django_staging" {
  name  = "django_staging"
  image = docker_image.django_staging.image_id

  ports {
    internal = 443
    external = var.backend_port
  }

  networks_advanced {
    name = docker_network.ditter_network.name
  }

  env = ["SECRET_KEY=${var.secret_key}"]

  depends_on = [docker_container.postgres_staging]

  volumes {
    container_path = "/etc/nginx/nginx.conf"
    host_path      = "${path.cwd}/../units/django_nginx.conf"
  }

  volumes {
    container_path = "/etc/letsencrypt/live/ditter.rand0m.one/fullchain.pem"
    host_path      = "${path.cwd}/../units/cert.pem"
  }

  volumes {
    container_path = "/etc/letsencrypt/live/ditter.rand0m.one/privkey.pem"
    host_path      = "${path.cwd}/../units/key.pem"
  }
}

resource "docker_container" "vue_staging" {
  name  = "vue_staging"
  image = docker_image.vue_staging.image_id

  ports {
    internal = 443
    external = 443
  }

  ports {
    internal = 80
    external = 80
  }

  volumes {
    container_path = "/etc/nginx/nginx.conf"
    host_path      = "${path.cwd}/../units/vue_nginx.conf"
  }

  volumes {
    container_path = "/etc/letsencrypt/live/ditter.rand0m.one/fullchain.pem"
    host_path      = "${path.cwd}/../units/cert.pem"
  }

  volumes {
    container_path = "/etc/letsencrypt/live/ditter.rand0m.one/privkey.pem"
    host_path      = "${path.cwd}/../units/key.pem"
  }
}

resource "docker_container" "postgres_staging" {
  name     = "postgres_staging"
  hostname = "ditterdb"
  image    = docker_image.postgres_staging.image_id

  env = ["POSTGRES_PASSWORD=${var.db_password}", "POSTGRES_USER=${var.db_username}", "POSTGRES_DB=${var.db_name}", "PGDATA=/var/lib/postgresql/data/pgdata"]

  networks_advanced {
    name = docker_network.ditter_network.name
  }

  volumes {
    container_path = "/var/lib/postgresql/data"
    host_path      = var.db_storage_path
  }
}