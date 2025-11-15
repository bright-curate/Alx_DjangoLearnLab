from django.urls import path
from .views import list_books, LibraryDetailView  # required import
from django.urls import path
from .views import list_books, LibraryDetailView, register, login_view, logout_view  # add these
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # class-based view
 
    # ✅ Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based URLs
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    path('books/add/', views.add_book, name='add_book/'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book/'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
]

