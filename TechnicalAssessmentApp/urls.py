from django.urls import path

from TechnicalAssessmentApp import views

urlpatterns = [
    path('', views.list_of_books, name='list_of_books'),
    path('books/post/', views.books_form, name='book_register'),
    path('books/delete_book/<int:id>/', views.books_delete, name='book_delete'),
    path('books/list/', views.list_of_books, name='list_of_books'),
    path('books/update/<int:id>/', views.books_form, name='book_update'),
    path('books/retrieve_book_details/<int:id>', views.retrieve_project, name="retrieve_project"),

    path('authors/aut', views.author_form, name='author_register'),
    path('authors/<int:id>/', views.author_form, name='author_update'),
    path('authors/delete/<int:id>/', views.author_delete, name='author_delete'),
    path('authors/authorlist/', views.list_of_authors, name='list_of_authors'),
    path('authors/retrieve_author_details/<int:id>', views.retrieve_author_project, name="retrieve_author_details"),

]
