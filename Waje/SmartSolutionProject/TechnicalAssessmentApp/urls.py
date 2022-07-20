from django.urls import path, include
from . import views
from TechnicalAssessmentApp import views

urlpatterns = [
    path('bk', views.books_form, name='book_register'),
    path('delete/<int:id>/', views.books_delete, name='book_delete'),
    path('list/', views.list_of_books, name='list_of_books'),
    path('<int:id>/', views.books_form, name='book_update'),

    path('aut', views.author_form, name='author_register'),
    path('<int:id>/', views.author_form, name='author_update'),
    path('delete/<int:id>/', views.author_delete, name='author_delete'),
    path('authorlist/', views.list_of_authors, name='list_of_authors'),

]
