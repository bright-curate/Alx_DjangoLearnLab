from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book


# ----------------------------------------------------
# Book Admin
# ----------------------------------------------------
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')


# ----------------------------------------------------
# Custom User Admin
# ----------------------------------------------------
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
