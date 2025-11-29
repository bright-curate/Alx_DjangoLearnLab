from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


"""
ListView:
- Allows anyone (authenticated or not) to view all books.
- Uses ListAPIView.
"""
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


 # Filtering, Searching, Ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

 # Fields allowed for filtering
    filterset_fields = ['title', 'author', 'publication_year']

# Fields allowed for searching
    search_fields = ['title', 'author__name']

# Fields allowed for ordering
    ordering_fields = ['title', 'publication_year']

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

