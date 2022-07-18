from django.shortcuts import render, redirect
from TechnicalAssessmentApp.forms import Booksform
from .models import Book


def list_of_books(request):
    context = {'list_of_books': Book.objects.all()}
    return render(request, "List.html", context)


def books_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = Booksform()
        else:
            book = Book.objects.get(pk=id)
            form = Booksform(instance=book)
        return render(request, "Register.html", {'form': form})
    else:
        if id == 0:
            form = Booksform(request.POST)
        else:
            book = Book.objects.get(pk=id)
            form = Booksform(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books/list')


def books_delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('/books/list')
