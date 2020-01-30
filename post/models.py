from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    title = models.CharField(
        max_length=80,
    )

    content = models.TextField()

    created = models.DateTimeField(
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        auto_now=True
    )

    shared = models.ForeignKey(
        verbose_name='shared post',
        to='self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sharing_posts'
    )

    def __str__(self):
        return f"Post ID {self.pk} from {self.author}: {self.title[:50]} ..."
