from django.urls import path, include
from .views import register, login, profile

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("profile/", profile, name="profile"),
    path("api/", include("accounts.urls")),
    path("api/", include("posts.urls")),
]
