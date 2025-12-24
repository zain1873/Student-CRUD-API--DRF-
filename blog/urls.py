from django.urls import path
from .views import BlogsView, CommentsView, BlogDetailView, CommentDetailView

urlpatterns = [
    path("blogs/", BlogsView.as_view(), name="blog-view"),
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),
    path("comments/", CommentsView.as_view(), name="comment-view"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail")
]
