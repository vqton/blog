from django.contrib import admin
import json
from django.db import transaction
from blog.models import Post

# Register your models here.



admin.site.register(Post)