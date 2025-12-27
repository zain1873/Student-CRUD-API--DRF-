from django.urls import path
from .views import (
    index, 
    post_list, 
    BlogsView, 
    CommentsView, 
    BlogDetailView, 
    CommentDetailView
)

urlpatterns = [
    # Frontend page
    path('index/', index, name='index'),

    # Simple posts API (GET/POST example)
    path('posts/', post_list, name='post_list'),

    # Blog API views
    path("blogs/", BlogsView.as_view(), name="blog-view"),
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),

    # Comment API views
    path("comments/", CommentsView.as_view(), name="comment-view"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
]
