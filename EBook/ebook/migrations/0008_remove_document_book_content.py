# Generated by Django 4.2.1 on 2024-07-10 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0007_document_book_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='book_content',
        ),
    ]