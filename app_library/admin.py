from django.contrib import admin
from .models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """ Admin panel for Book model """

    list_display = [field.name for field in Book._meta.fields]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """ Admin panel for Author model """

    list_display = [field.name for field in Author._meta.fields]
