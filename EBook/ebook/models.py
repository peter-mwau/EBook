from django.db import models
from django.db.models.deletion import CASCADE

class BookContent(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
    
# class Document(models.Model):
#     file = models.FileField(upload_to='documents/')

class Document(models.Model):
    # Your existing fields...
    # book_content = models.ForeignKey(BookContent, on_delete=CASCADE)
    file = models.FileField(upload_to='documents/')
    filename = models.CharField(max_length=255, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.filename = self.file.name
        super(Document, self).save(*args, **kwargs)
