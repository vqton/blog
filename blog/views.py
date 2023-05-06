from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from blog.models import Post

from taggit.models import Tag


# Create your views here.
def home(request):
    posts = Post.objects.all()
    # print(posts.count())
    context = {"posts": posts}

    return render(request, "blog/index.html", context)


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    ctx = {"post": post}
    return render(request, "blog/post_detail.html", ctx)


# def tagged_posts(request, slug):
#     tag = get_list_or_404(TaggedItem, slug=slug)
#     posts = tag.posts.all()
#     context = {"tag": tag, "posts": posts}
#     return render(request, "blog/tagged_post_list.html", context)


class TaggedPostListView(ListView):
    model = Post
    template_name = "blog/tagged_post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        tag_slug = self.kwargs.get("slug")
        queryset = Post.objects.filter(tags__name=tag_slug).order_by("-date_posted")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_slug = self.kwargs.get("slug")
        # tag = get_object_or_404(Tag, slug=tag_slug)
        tag = Tag.objects.get(slug=tag_slug)
        context['tag'] = tag
        return context