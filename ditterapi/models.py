import uuid
from django.db import models
from django.contrib.auth import get_user_model


class Author(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)
    display_name = models.TextField()

    def format(self):
        return {
            "author_username": self.username,
            "author_display_name": self.display_name,
        }

    def __str__(self):
        return f"@{self.username} ({self.uuid})"


class Dweet(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)

    def format(self):
        liked_by = [
            like.user.username for like in DweetLike.objects.filter(dweet_id=self.uuid)
        ]
        return {
            "uuid": str(self.uuid),
            "content": self.content,
            "likes": self.likes(),
            "liked_by": liked_by,
            "author_username": self.author.username,
            "author_display_name": self.author.display_name,
            "created_on": self.created_on,
        }

    def likes(self):
        return DweetLike.objects.filter(dweet=self).count()

    def __str__(self):
        return f"@{self.author.username}: {self.content} ({str(self.uuid)})"


class DweetLike(models.Model):
    dweet = models.ForeignKey("Dweet", on_delete=models.CASCADE)
    user = models.ForeignKey("Author", on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            "dweet",
            "user",
        )
