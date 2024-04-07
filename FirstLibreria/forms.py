from django import forms
from .models import Genre, Author, Publisher, Book

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'date_of_birth']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset = Author.objects.all(),
        empty_label = "Selecciona un Autor"
    )
    genre = forms.ModelChoiceField(
        queryset = Genre.objects.all(),
        empty_label = "Selecciona un Genero"
    )
    publisher = forms.ModelChoiceField(
        queryset = Publisher.objects.all(),
        empty_label = "Selecciona una Editorial"
    )
    class Meta:
        model = Book
        fields = ['name', 'author', 'genre', 'publisher']
