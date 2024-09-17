from .models import Book, Author, Genre
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title', 'author', 'genre','publication_date','isbn']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['genre']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['author']