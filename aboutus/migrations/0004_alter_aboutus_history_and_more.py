# Generated by Django 4.2 on 2023-04-27 03:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("aboutus", "0003_alter_aboutus_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aboutus",
            name="history",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="aboutus",
            name="mission_statement",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="aboutus",
            name="vision_statement",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
