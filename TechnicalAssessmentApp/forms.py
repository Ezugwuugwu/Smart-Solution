from django import forms

from .models import Book, Author
from django.forms import MultiWidget, TextInput


class Booksform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'isbn', 'author']


class Authorform(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']