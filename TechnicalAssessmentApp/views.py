from django.shortcuts import render, redirect

from TechnicalAssessmentApp.authorForms import AuthorForm
from TechnicalAssessmentApp.forms import Booksform
from .models import Book, Author
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token


def list_of_books(request):
    context = {'list_of_books': Book.objects.all()}
    return render(request, "List.html", context)


@csrf_exempt
@requires_csrf_token
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

@csrf_exempt
@requires_csrf_token
def books_delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('/books/list')


def list_of_authors(request):
    context = {'list_of_authors': Author.objects.all()}
    return render(request, "AuthorList.html", context)


@csrf_exempt
@requires_csrf_token
def author_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            authorForm = AuthorForm()
        else:
            author = Author.objects.get(pk=id)
            authorForm = AuthorForm(instance=author)
        return render(request, "AuthorRegister.html", {'form': authorForm})
    else:
        if id == 0:
            authorForm = AuthorForm(request.POST)
        else:
            author = Author.objects.get(pk=id)
            authorForm = AuthorForm(request.POST, instance=author)
        if authorForm.is_valid():
            authorForm.save()
            return redirect('/authors/authorlist')

@csrf_exempt
@requires_csrf_token
def author_delete(request, id):
    author = Author.objects.get(pk=id)
    author.delete()
    return redirect('/authors/authorlist')


def retrieve_project(request, id):
    if Book.objects.filter(pk=id).exists():
        project = Book.objects.get(pk=id)
    else:
        project = {}
    return render(request, "Book_details.html", {'project': project})
