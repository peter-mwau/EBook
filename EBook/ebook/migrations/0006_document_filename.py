# Generated by Django 4.2.1 on 2024-07-08 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0005_remove_document_book_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='filename',
            field=models.CharField(default=1, editable=False, max_length=255),
            preserve_default=False,
        ),
    ]