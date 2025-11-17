from bookshelf.models import Book

books = Book.objects.get(title="1984")
for b in books:
    print(b.title, b.author, b.publication_year)

# Output:
# 1984 George Orwell 1949
