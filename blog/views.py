from django.shortcuts import render
from django.views.generic import DetailView
from blog.models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {"posts": posts}

    return render(request, "blog/index.html", context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'