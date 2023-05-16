# myapp/management/commands/bulk_insert_posts.py

import json
from django.core.management.base import BaseCommand
from blog.models import Post

class Command(BaseCommand):
    help = 'Bulk insert posts from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        with open(file_path) as f:
            data = json.load(f)
            

        for post_data in data:
            post = Post(title=post_data['title'], content=post_data['content'], image=post_data['image'])
            post.save()
            # Add other fields like tags, image, etc. as per your data structure

        self.stdout.write(self.style.SUCCESS('Successfully inserted posts.'))
