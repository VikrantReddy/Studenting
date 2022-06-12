from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Post(models.Model):

    class Featured(models.TextChoices):
        MAIN_FEATURE = "LF",_("Left Featured")
        SIDE_FEATURE =  "RF",_("Right Featured")
        NOT_FEATURE = "NO",_("Not Featured")

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    image = models.ImageField(upload_to="media")
    author = models.CharField(max_length=64)
    topic = models.CharField(max_length=64)
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    featured = models.CharField(
    max_length=2,
    choices=Featured.choices,
    default=Featured.NOT_FEATURE
    )
    feature_index = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title
