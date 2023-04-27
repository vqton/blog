# Generated by Django 4.2 on 2023-04-27 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AboutUs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="about_us_images/")),
                ("mission_statement", models.TextField()),
                ("vision_statement", models.TextField()),
                ("history", models.TextField()),
                ("founding_year", models.IntegerField()),
            ],
        ),
    ]
