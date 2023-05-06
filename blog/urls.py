from django.urls import path
from . import views
from django.urls import reverse
from .views import TaggedPostListView


urlpatterns = [
    path("", views.home, name="home"),
    path("post/<int:post_pk>/", views.post_detail, name="post_detail"),
    path('tag/<slug:slug>/', TaggedPostListView.as_view(), name='tagged_posts'),
    # path('tag/<slug:slug>/', views.tagged_posts, name='tagged_posts'),
]
