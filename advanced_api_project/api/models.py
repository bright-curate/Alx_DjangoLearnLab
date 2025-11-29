from django.db import models
from django.utils import timezone

"""
Author Model:
- Stores basic info about an author.
"""

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


"""
Book Model:
- Stores title, publication year, and the author.
- One-to-many relationship (one author → many books)
"""

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return self.title

