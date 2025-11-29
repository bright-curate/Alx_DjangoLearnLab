from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User

from .models import Book, Author


class BookAPITests(APITestCase):

    def setUp(self):
        """
        Setup test environment:
        - Create test user
        - Authenticate user when needed
        - Create authors and books for filtering/searching tests
        """

        self.client = APIClient()

        # User for authenticated actions (create, update, delete)
        self.user = User.objects.create_user(
            username="testuser", password="testpassword123"
        )

        # Create Authors
        self.author1 = Author.objects.create(name="John Doe")
        self.author2 = Author.objects.create(name="Mary Jane")

        # Create Books
        self.book1 = Book.objects.create(
            title="Alpha Book",
            publication_year=2001,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Beta Book",
            publication_year=1999,
            author=self.author2
        )

    # -------------------------------------------------------
    # LIST VIEW TEST
    # -------------------------------------------------------
    def test_list_books(self):
        """
        Ensure the list endpoint returns all books.
        """
        url = reverse("book-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # -------------------------------------------------------
    # DETAIL VIEW TEST
    # -------------------------------------------------------
    def test_retrieve_single_book(self):
        """
        Ensure retrieving a single book by ID works.
        """
        url = reverse("book-detail", kwargs={"pk": self.book1.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Alpha Book")

    # -------------------------------------------------------
    # CREATE VIEW TEST (requires authentication)
    # -------------------------------------------------------
    def test_create_book_authenticated(self):
        """
        Ensure authenticated users can create books.
        """
        self.client.login(username="testuser", password="testpassword123")

        url = reverse("book-create")
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author1.id
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot create books.
        """
        url = reverse("book-create")
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2024,
            "author": self.author1.id
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -------------------------------------------------------
    # UPDATE VIEW TEST
    # -------------------------------------------------------
    def test_update_book(self):
        """
        Ensure authenticated users can update a book.
        """
        self.client.login(username="testuser", password="testpassword123")

        url = reverse("book-update", kwargs={"pk": self.book1.id})
        data = {"title": "Updated Title", "publication_year": 2001, "author": self.author1.id}

        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_book = Book.objects.get(id=self.book1.id)
        self.assertEqual(updated_book.title, "Updated Title")

    # -------------------------------------------------------
    # DELETE VIEW TEST
    # -------------------------------------------------------
    def test_delete_book(self):
        """
        Ensure authenticated users can delete a book.
        """
        self.client.login(username="testuser", password="testpassword123")

        url = reverse("book-delete", kwargs={"pk": self.book2.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # -------------------------------------------------------
    # FILTERING TEST
    # -------------------------------------------------------
    def test_filter_books_by_title(self):
        """
        Test filtering functionality.
        """
        url = reverse("book-list")
        response = self.client.get(url + "?title=Alpha Book")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # -------------------------------------------------------
    # SEARCH TEST
    # -------------------------------------------------------
    def test_search_books_by_title(self):
        """
        Test search functionality using SearchFilter.
        """
        url = reverse("book-list")
        response = self.client.get(url + "?search=Alpha")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # -------------------------------------------------------
    # ORDERING TEST
    # -------------------------------------------------------
    def test_order_books_by_publication_year(self):
        """
        Test ordering functionality.
        """
        url = reverse("book-list")
        response = self.client.get(url + "?ordering=publication_year")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data[0]["title"],
            "Beta Book"  # Oldest = first
        )
