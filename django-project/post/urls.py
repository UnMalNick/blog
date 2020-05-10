from django.urls import path, include, re_path

from post.views import PostView


urlpatterns = [
    path('<slug:category_slug>/<slug:post_slug>/', PostView.as_view(), name="post-detail")
]
