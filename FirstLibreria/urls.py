from django.urls import path
from . import views
from .views import GenreListView

urlpatterns = [
    path('author', views.author_list, name='author_list'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('authors/new/', views.author_new, name='author_new'),
    path('authors/<int:pk>/edit/', views.author_edit, name='author_edit'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author_delete'),

    path('genre', views.genre_list, name='genre_list'),
    path('genres/new/', views.genre_new, name='genre_new'), 
    path('genres/<int:pk>/', views.genre_detail, name='genre_detail'),
    path('genres/<int:pk>/edit/', views.genre_edit, name='genre_edit'),
    path('genres/<int:pk>/delete/', views.genre_delete, name='genre_delete'),

    path('publisher', views.publisher_list, name='publisher_list'),
    path('publishers/<int:pk>/', views.publisher_detail, name='publisher_detail'),
    path('publishers/new/', views.publisher_new, name='publisher_new'),
    path('publishers/<int:pk>/edit/', views.publisher_edit, name='publisher_edit'),
    path('publishers/delete/<int:pk>/', views.publisher_delete, name='publisher_delete'),

    path('', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/new/', views.book_new, name='book_new'),
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('genre/', GenreListView.as_view(), name='genre_list'),
]
