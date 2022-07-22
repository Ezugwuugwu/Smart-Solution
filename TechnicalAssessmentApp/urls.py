from django.urls import path

from TechnicalAssessmentApp import views

urlpatterns = [
    path('get', '', views.list_of_books, name='list_of_books'),
    path('/', views.list_of_books, name='list_of_books'),
    path('post', views.books_form, name='book_register'),
    path('delete_book/<int:id>/', views.books_delete, name='book_delete'),
    path('list/', views.list_of_books, name='list_of_books'),
    path('update/<int:id>/', views.books_form, name='book_update'),
    path('retrieve_book_details/<int:id>', views.retrieve_project, name="retrieve_project"),

    path('aut', views.author_form, name='author_register'),
    path('<int:id>/', views.author_form, name='author_update'),
    path('delete/<int:id>/', views.author_delete, name='author_delete'),
    path('authorlist/', views.list_of_authors, name='list_of_authors'),

]
