from django import forms
from .models import Book, Author


class Booksform(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        # u can also do
        # fields = ('Book name', 'isbn', 'author'), just to select fields


class Authorform(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
