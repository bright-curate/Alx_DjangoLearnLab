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