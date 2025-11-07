from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()  # uses related_name='books'
    except Author.DoesNotExist:
        return []


# Query 2: List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []


# Query 3: Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# Example usage (only for testing — not executed automatically)
if __name__ == "__main__":
    # Example data
    for book in books_by_author("J.K. Rowling"):
        print("Book by J.K. Rowling:", book.title)

    for book in books_in_library("Central Library"):
        print("Book in Central Library:", book.title)

    librarian = librarian_for_library("Central Library")
    if librarian:
        print("Librarian for Central Library:", librarian.name)
    else:
        print("No librarian assigned.")
