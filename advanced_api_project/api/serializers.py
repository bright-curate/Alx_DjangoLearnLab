from rest_framework import serializers
from datetime import datetime
from .models import Author, Book

"""
BookSerializer:
- Serializes the Book model.
- Includes custom validation to ensure the publication year
  is not greater than the current year.
"""

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


"""
AuthorSerializer:
- Serializes the Author model.
- Includes a nested BookSerializer to show all books by that author.
"""

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  
    # Uses related_name='books' from the Book model

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
