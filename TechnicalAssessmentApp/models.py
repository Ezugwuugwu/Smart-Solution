from django.db import models


class Author(models.Model):
    first_name = models.TextField(max_length=10)
    last_name = models.TextField(max_length=10)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Book(models.Model):
    book_name = models.TextField(max_length=20)
    isbn = models.TextField(max_length=13)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
