from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    class Meta:
        db_table = 'inventory'

    
    def __str__(self):
        return self.title
