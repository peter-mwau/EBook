from django.shortcuts import render
import requests
from .models import BookContent


def home(request):
    # content = BookContent.objects.all()
    # get title from BookContent
    title = BookContent.objects.values_list('title', flat=True)
    content = BookContent.objects.values_list('content', flat=True)

    title = title[0]
    content = content[0]

    # save to dbase
    # r = BookContent(title=title, content=content)
    # r.save()

    context ={
        'titles': title,
        'content': content,
    }
    return render(request, 'home2.html', context)

