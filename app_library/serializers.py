from .models import Book, Author
from rest_framework import serializers as s


class BookSerializer(s.HyperlinkedModelSerializer):
    """ Serializer of Book model """
    class Meta:
        model = Book
        fields = [field.name for field in model._meta.fields]


class AuthorSerializer(s.HyperlinkedModelSerializer):
    """ Serializer of Author model """
    class Meta:
        model = Author
        fields = [field.name for field in model._meta.fields]
