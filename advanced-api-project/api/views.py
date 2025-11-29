from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


"""
ListView:
- Allows anyone (authenticated or not) to view all books.
- Uses ListAPIView.
"""
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


"""
DetailView:
- Retrieve a single book using its ID (pk).
- Read-only access for everyone.
"""
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


"""
CreateView:
- Only authenticated users can create books.
- Uses CreateAPIView.
- Custom validation handled in the serializer.
"""
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

def perform_create(self, serializer):
    """
    Custom behavior for creating books:
    - You could automatically assign the author to the logged-in user
      if your system supports user authorship.
    """
    serializer.save()



"""
UpdateView:
- Only authenticated users can update books.
- Uses UpdateAPIView.
"""
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

def perform_update(self, serializer):
    """
    Custom behavior for updating books:
    - Add hooks for logging or restricting updates.
    """
    serializer.save()



"""
DeleteView:
- Only authenticated users can delete books.
- Uses DestroyAPIView.
"""
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

