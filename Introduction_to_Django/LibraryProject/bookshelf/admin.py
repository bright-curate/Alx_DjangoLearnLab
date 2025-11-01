from django.contrib import admin

# Register your models here.

from .models import Book  # import the Book model

# Register Book model with custom admin display
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show
    list_filter = ('publication_year', 'author')  # filters on the right side
    search_fields = ('title', 'author')  # search bar at the top
