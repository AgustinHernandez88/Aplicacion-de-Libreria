from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from .models import Author, Genre, Publisher, Book
from .forms import AuthorForm, GenreForm, PublisherForm, BookForm
from django.views.generic import ListView


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'FirstLibreria/author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'FirstLibreria/author_detail.html', {'author': author})

def author_new(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'FirstLibreria/author_edit.html', {'form': form})

def author_edit(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'FirstLibreria/author_edit.html', {'form': form, 'author': author})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    
    try:
        author.delete()
        messages.success(request, 'Autor eliminado exitosamente.', extra_tags='one-time')
    except ProtectedError:
        messages.error(request, 'Hubo un problema al eliminar el autor porque está relacionado con libros.', extra_tags='one-time')
    
    return redirect('author_list')

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'FirstLibreria/genre_list.html', {'genres': genres})

def genre_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    return render(request, 'FirstLibreria/genre_detail.html', {'genre': genre})

def genre_new(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm()
    return render(request, 'FirstLibreria/genre_edit.html', {'form': form})

def genre_edit(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm(instance=genre)
    return render(request, 'FirstLibreria/genre_edit.html', {'form': form, 'genre': genre})

def genre_delete(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    
    try:
        genre.delete()
        messages.success(request, 'Género eliminado exitosamente.', extra_tags='one-time')
    except ProtectedError:
        messages.error(request, 'No se puede eliminar este género porque está relacionado con libros.', extra_tags='one-time')
    
    return redirect('genre_list')





def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'FirstLibreria/publisher_list.html', {'publishers': publishers})

def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    return render(request, 'FirstLibreria/publisher_detail.html', {'publisher': publisher})

def publisher_new(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
    else:
        form = PublisherForm()
    return render(request, 'FirstLibreria/publisher_edit.html', {'form': form})

def publisher_edit(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'FirstLibreria/publisher_edit.html', {'form': form, 'publisher': publisher})

def publisher_delete(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    
    try:
        publisher.delete()
        messages.success(request, 'Editorial eliminada exitosamente.', extra_tags='one-time')
    except ProtectedError:
        messages.error(request, 'No se puede eliminar esta editorial porque está relacionada con libros.', extra_tags='one-time')
    
    return redirect('publisher_list')




def book_list(request):
    books = Book.objects.all()
    return render(request, 'FirstLibreria/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'FirstLibreria/book_detail.html', {'book': book})

def book_new(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'FirstLibreria/book_edit.html', {'form': form})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'FirstLibreria/book_edit.html', {'form': form, 'book': book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    messages.success(request, 'Libro eliminado exitosamente.', extra_tags='one-time')

    return redirect('book_list')










class GenreListView(ListView):
    model = Genre
    template_name = 'FirstLibreria/genre_list.html'
    context_object_name = 'genres'

def genre_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    return render(request, 'FirstLibreria/genre_detail.html', {'genre': genre})

def genre_new(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm()
    return render(request, 'FirstLibreria/genre_edit.html', {'form': form})

def genre_edit(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm(instance=genre)
    return render(request, 'FirstLibreria/genre_edit.html', {'form': form, 'genre': genre})

def genre_delete(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    
    try:
        genre.delete()
        messages.success(request, 'Género eliminado exitosamente.', extra_tags='one-time')
    except ProtectedError:
        messages.error(request, 'Hubo un problema al eliminar el género porque está relacionado con libros.', extra_tags='one-time')
    
    return redirect('genre_list')