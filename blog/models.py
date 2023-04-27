from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
from django.utils.text import slugify
from django.utils import timezone
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = RichTextField()
    slug = models.SlugField(unique=True, blank=True)
    content = RichTextField()
    tags = TaggableManager()
    image = models.ImageField(upload_to="blog/images/", null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})
