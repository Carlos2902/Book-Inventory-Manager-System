import csv
import json
from django.contrib import admin
from .models import Book, Author, Genre
from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder



class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_date', 'isbn')
    list_filter = ('author', 'genre', 'publication_date')
    search_fields = ('title', 'author__name', 'genre__name', 'isbn')  
    
    # Function  to export selected books as CSV
    def export_books_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=books.csv'
        writer = csv.writer(response)
        writer.writerow(['Title', 'Author', 'Genre', 'Publication Date', 'ISBN'])
        
        for book in queryset:
            writer.writerow([book.title, book.author.name, book.genre.name, book.publication_date, book.isbn])
        
        return response
    
    export_books_csv.short_description = "Export Selected Books as CSV"
    
    #function to export as JSON
    def export_books_json(self, request, queryset):
        books = list(queryset.values('title', 'author__name', 'genre__name', 'publication_date', 'isbn'))
        response = HttpResponse(
            json.dumps(books, cls=DjangoJSONEncoder, indent=2),
            content_type='application/json'
        )
        response['Content-Disposition'] = 'attachment; filename=books.json'
        return response
    
    export_books_json.short_description = "Export Selected Books as JSON"

    actions = [export_books_csv, export_books_json]

    
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    





admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
