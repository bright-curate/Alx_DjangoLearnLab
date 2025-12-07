Authentication System Documentation — django_blog


 1. Authentication Overview

The project uses Django's built-in authentication framework, combined with custom views and forms, to provide:

User registration

Login & Logout

Profile viewing and editing

Secure password handling

CSRF-protected forms

Django handles password hashing and session authentication automatically.


 2. Components Implemented
✔ Custom Registration Form

Built using Django’s UserCreationForm, extended to include email.

✔ Authentication Views

UserLoginView → login

UserLogoutView → logout

register() → new user sign-up

profile() → view + update user details

✔ URL Endpoints
URL Path	View	Purpose
/login/	LoginView	User login
/logout/	LogoutView	Logout confirmation
/register/	register()	Create new account
/profile/	profile()	View/edit profile

3. Templates

The following templates are included:

login.html

logout.html

register.html

profile.html

All templates use Django's templating system and static CSS.

 4. Security Measures

The authentication system includes:

CSRF protection for all forms

Django password hashing

Login required for profile access

Safe user data handling

No passwords are stored or processed in plain text.

 5. How to Test Authentication

Run server:

python manage.py runserver


Then test:

✔ Registration

Visit /register/

Create a new user

User should be automatically logged in

✔ Login

Visit /login/

Enter username/password

Redirect to profile

✔ Logout

Visit /logout/

Session should clear

✔ Profile

Must be logged in

Update email

Email should save successfully

 6. Files Added/Modified
Python Files

blog/forms.py

blog/views.py

blog/urls.py

Templates

blog/templates/blog/login.html

blog/templates/blog/logout.html

blog/templates/blog/register.html

blog/templates/blog/profile.html

## Blog Post Management (CRUD)

This app provides full CRUD for blog posts.

### URLs
- `GET /posts/` — List all posts
- `GET /posts/<pk>/` — View a single post
- `GET/POST /posts/new/` — Create new post (authenticated users only)
- `GET/POST /posts/<pk>/edit/` — Edit post (only author)
- `GET/POST /posts/<pk>/delete/` — Delete post (only author)

### Permissions
- Anyone can view the list and details.
- Only authenticated users can create posts.
- Only the author of a post can edit or delete it.

### Run locally
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


## Comment System

### Overview
- Users can read comments for each post.
- Authenticated users can add comments, edit their own comments, and delete their own comments.

### URLs
- `POST /post/<post_id>/comments/new/` — create a comment (auth required)
- `GET/POST /post/comments/<pk>/edit/` — edit comment (author only)
- `GET/POST /post/comments/<pk>/delete/` — delete comment (author only)

### Usage
- Comments appear on the post detail page.
- Unauthenticated users see a prompt to login for posting.
- CSRF protection enforced via `{% csrf_token %}`.
- Only comment authors can edit or delete comments.

### Running Tests
```bash
python manage.py test blog.tests_comments

### Tagging & Search

**Tagging**
- Add tags to posts when creating/editing using the "Tags" input (comma-separated).
- Tags are created automatically if they don't exist.
- Each post shows its tags; clicking a tag shows all posts with that tag: `/tags/<tag_name>/`.

**Search**
- Use the search box (site header or posts list) to search post titles, content, and tags.
- Example: `/post/?q=django` or `/search/?q=api`
