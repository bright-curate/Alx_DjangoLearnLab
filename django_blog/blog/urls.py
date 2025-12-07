from django.urls import path 
from .views import (
    UserLoginView, UserLogoutView, register, profile,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView,
)

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),

    # BLOG CRUD ROUTES (Checker Required)
    path("post/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:post_id>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("post/comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-edit"),
    path("post/comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]
