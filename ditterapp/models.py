import uuid
from django.db import models


# Create your models here.
class Author(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)
    display_name = models.TextField()

    def format(self):
        return {
            "author_id": self.uuid,
            "author_display_name": self.display_name,
        }

    def __str__(self):
        return f"@{self.username} ({self.uuid})"


class Dweet(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.PositiveBigIntegerField()
    created_on = models.DateTimeField()

    def format(self):
        return {
            "uuid": str(self.uuid),
            "content": self.content,
            "likes": self.likes,
            "author_id": self.author.uuid,
            "author_username": self.author.username,
            "author_display_name": self.author.display_name,
            "created_on": self.created_on,
        }

    def __str__(self):
        return f"@{self.author.username}: {self.content}"
