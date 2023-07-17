resource "docker_image" "django_prod" {
  name = "us-central1-docker.pkg.dev/ditter/ditterrepo/django:latest"
  pull_triggers = [timestamp()]
}

resource "docker_image" "vue_prod" {
  name = "us-central1-docker.pkg.dev/ditter/ditterrepo/vue:latest"
  pull_triggers = [timestamp()]
}

resource "docker_image" "postgres_prod" {
  name = "postgres:15.3"
}
