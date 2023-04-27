from django.db import models
from ckeditor.fields import RichTextField

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    # description = models.TextField()
    description = RichTextField()
    image = models.ImageField(upload_to="about_us_images/")
    mission_statement = RichTextField()
    vision_statement = RichTextField()
    history = RichTextField()
    founding_year = models.IntegerField()

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.title
