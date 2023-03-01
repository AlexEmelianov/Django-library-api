from rest_framework import viewsets
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """ API view of Book model """

    serializer_class = BookSerializer

    def get_queryset(self):
        """ Return Book queryset filtered by query params """

        queryset = Book.objects.all()
        filters = {key: value for key, value in self.request.query_params.items() if key != 'page'}
        if filters:
            queryset = queryset.filter(**filters)
        return queryset


class AuthorViewSet(viewsets.ModelViewSet):
    """ API view of Author model """

    serializer_class = AuthorSerializer

    def get_queryset(self):
        """ Return Author queryset filtered by query params """

        queryset = Author.objects.all()
        filters = {key: value for key, value in self.request.query_params.items() if key != 'page'}
        if filters:
            queryset = queryset.filter(**filters)
        return queryset
