from django.contrib import admin
from .models import BookContent, Document

class BookContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')  # Adjust these fields based on your BookContent model

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'filename', 'file')  # Adjust these fields based on your Document model

# Register your models here.
admin.site.register(BookContent, BookContentAdmin)
admin.site.register(Document, DocumentAdmin)