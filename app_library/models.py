from django.db import models as m


class Book(m.Model):
    """ Book model """

    title = m.CharField(max_length=100, verbose_name='title')
    release_year = m.DecimalField(max_digits=4, decimal_places=0, verbose_name='release year')
    n_pages = m.DecimalField(max_digits=6, decimal_places=0, verbose_name='number of pages')
    isbn = m.CharField(max_length=30, unique=True, verbose_name='ISBN')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-release_year']


class Author(m.Model):
    """ Author model """

    first_name = m.CharField(max_length=50, verbose_name='first name')
    last_name = m.CharField(max_length=50, verbose_name='last name')
    birthdate = m.DateField(verbose_name='date of birth')
    books = m.ManyToManyField(Book)

    class Meta:
        ordering = ['pk']
