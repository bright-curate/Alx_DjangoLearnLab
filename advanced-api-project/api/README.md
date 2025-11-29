# Advanced API Project — Generic Views & Permissions

This project implements CRUD operations for the Book model using
Django REST Framework’s generic views and permissions.

## Endpoints

| Endpoint | Method | Permission | Description |
|---------|--------|------------|-------------|
| /api/books/ | GET | Public | List all books |
| /api/books/<pk>/ | GET | Public | Retrieve one book |
| /api/books/create/ | POST | Authenticated | Create a book |
| /api/books/<pk>/update/ | PUT/PATCH | Authenticated | Update a book |
| /api/books/<pk>/delete/ | DELETE | Authenticated | Delete a book |

## Permissions

- Authenticated users: Can create, update, delete
- Unauthenticated users: Can view only

## Customizations

- Nested serializers for Author → Books
- Validation: publication_year cannot be in the future
- Custom hooks available: perform_create, perform_update

# Filtering
/books/?title=SomeTitle
/books/?publication_year=2023

# Searching
/books/?search=tolkien

# Ordering
/books/?ordering=title
/books/?ordering=-publication_year


Advanced API Project – Book API Documentation
1. Project Overview

This project is an API for managing Books and Authors, built with Django REST Framework.

It supports:

CRUD operations on books

Nested relationships with authors

Filtering, searching, and ordering of books

Authentication and permissions for secure endpoints

2. API Endpoints
Endpoint	Method	Description	Permissions
/books/	GET	List all books	Public
/books/<id>/	GET	Retrieve details of a book by ID	Public
/books/create/	POST	Create a new book	Authenticated users
/books/update/<id>/	PUT	Update an existing book	Authenticated users
/books/delete/<id>/	DELETE	Delete a book	Authenticated users
Query Parameters

Filtering: ?title=BookTitle, ?author=AuthorID, ?publication_year=YYYY

Searching: ?search=BookTitle or ?search=AuthorName

Ordering: ?ordering=title or ?ordering=-publication_year



3. Testing Strategy

Unit tests are implemented to ensure functionality, data integrity, and permissions.

Key Areas Tested

CRUD Operations

Create, Read, Update, Delete

Verify correct HTTP status codes and response data

Filtering

Ensure API returns correct results when filtering by title, author, or publication year

Searching

Verify text searches on book titles and author names

Ordering

Test ascending/descending sorting by title and publication year

Permissions

Ensure authenticated endpoints reject unauthenticated requests

Verify list and detail endpoints are publicly accessible


4. Test Cases
Test Case	Description	Expected Result
test_list_books	List all books	Returns 200 OK, all books included
test_retrieve_book	Retrieve a single book by ID	Returns 200 OK, correct book data
test_create_book_authenticated	Authenticated user creates book	Returns 201 Created, book saved
test_create_book_unauthenticated	Unauthenticated user attempts create	Returns 401 Unauthorized
test_update_book	Authenticated user updates book	Returns 200 OK, changes persisted
test_delete_book	Authenticated user deletes book	Returns 204 No Content, book removed
test_filter_books_by_title	Filter by book title	Returns only books that match title
test_search_books_by_author	Search by author name	Returns matching books
test_order_books_by_year	Order books by publication year	Returns sorted list


5. Running Tests

Navigate to the project root:

cd advanced-api-project


Run all tests for the api app:

python manage.py test api


What happens:

Django creates a temporary test database

All tests in api/test_views.py are executed

Console shows which tests pass or fail


6. Interpreting Test Results

OK / Passed tests: The API behaves as expected

FAIL / Errors: Indicates mismatch between expected behavior and actual results (status codes, data, permissions)

Action: Inspect the failing test, fix the corresponding view, serializer, or permission, then rerun tests