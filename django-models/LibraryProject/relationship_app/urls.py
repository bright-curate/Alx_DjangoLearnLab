from django.urls import path
from .views import list_books, LibraryDetailView  # required import
from django.urls import path
from .views import list_books, LibraryDetailView, register, login_view, logout_view  # add these


urlpatterns = [
    path('books/', list_books, name='list_books'),  # function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # class-based view
 
    # ✅ Authentication URLs
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

