import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from blog.models import Post
from taggit.models import Tag
from django.core.files.uploadedfile import SimpleUploadedFile
import os


def search_files(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None


class Command(BaseCommand):
    help = "Bulk insert posts from a CSV file"

    def create_tags(self, tags_data):
        # Parse the tags data as a list of tags
        tags_list = tags_data.split(",")

        # Create or retrieve existing tags based on the provided data
        tags = []
        for tag_name in tags_list:
            tag, _ = Tag.objects.get_or_create(name=tag_name.strip())
            tags.append(tag)

        return tags

    def save_image_file(self, image_file_path):
        # Search for the image file in the media root directory
        media_root = settings.MEDIA_ROOT
        # image_path = os.path.join(media_root, image_file_path)

        absolute_path = search_files(media_root, image_file_path)
        # Check if the image file exists
        if os.path.exists(absolute_path):
            # Open and read the image file
            with open(absolute_path, "rb") as f:
                image_data = f.read()

            # Extract the image file name from the path
            image_name = os.path.basename(absolute_path)

            # Create a SimpleUploadedFile object
            image_file = SimpleUploadedFile(image_name, image_data)
            
            # Return the SimpleUploadedFile object
            return image_file

        return None

    def bulk_insert_posts(self, file_path):
        with open(file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                title = row["title"]
                content = row["content"]
                image_file_path = row["image"]
                tags_data = row["tags"]
                slug = row["slug"]

                # Check if a post with the same slug already exists
                if Post.objects.filter(slug=slug).exists():
                    self.stdout.write(
                        f'Skipping post with slug "{slug}" - Duplicate entry'
                    )
                    continue

                # Save the image file
                image = self.save_image_file(image_file_path)
                absPath = search_files(settings.MEDIA_ROOT + "/blog", image_file_path)

                # Create tags
                tags = self.create_tags(tags_data)

                # Create a new Post object
                post = Post(
                    title= title ,
                    content="<p>" + content + "</p>",
                    slug=slug,
                    image=absPath,
                )

                # Set the image field if available
                if image:
                    post.image.save(image_file_path, image, save=True)
                    post.image = f"blog\images\{image_file_path}"

                # Save the Post object to get a primary key value
                post.save()

                # Set the tags field if available
                if tags:
                    post.tags.add(*tags)
                
                os.remove(absPath)

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to the CSV file")

    def handle(self, *args, **options):
        file_path = options["file_path"]
        self.bulk_insert_posts(file_path)
        self.stdout.write(self.style.SUCCESS("Successfully inserted posts."))
