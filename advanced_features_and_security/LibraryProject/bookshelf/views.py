from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm


# ---------------------------------------------
# Required: book_list view
# ---------------------------------------------
@permission_required('bookshelf.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Required variable: "books"
    return render(request, 'bookshelf/book_list.html', {'books': books})


# ---------------------------------------------
# Required: raise_exception demonstration
# ---------------------------------------------
@permission_required('bookshelf.delete_book', raise_exception=True)
def raise_exception(request):
    return HttpResponse("You have permission to delete books.")


# ---------------------------------------------
# Required: books view (simple/demo)
# ---------------------------------------------
def books(request):
    books = Book.objects.all()   # Required variable: "books"
    output = ", ".join([book.title for book in books])
    return HttpResponse(f"Books: {output}")

