from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    author = models.CharField(max_length=64)
    topic = models.CharField(max_length=64)
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]
