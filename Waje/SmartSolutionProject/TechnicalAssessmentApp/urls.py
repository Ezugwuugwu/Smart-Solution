from django.urls import path, include
from . import views
from TechnicalAssessmentApp import views

urlpatterns = [
    path('', views.books_form, name='book_register'),
    path('<int:id>/', views.books_form, name='book_update'),
    path('delete/<int:id>/', views.books_delete, name='book_delete'),
    path('list/', views.list_of_books, name='list_of_books'),

]
