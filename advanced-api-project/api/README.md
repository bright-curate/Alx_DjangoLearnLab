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
