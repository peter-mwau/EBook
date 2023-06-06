from django.shortcuts import render
import requests
from .models import BookContent


def home(request):
    content = BookContent.objects.all()
    # get title from BookContent
    id = BookContent.objects.values_list('id', flat=True)
    title = BookContent.objects.values_list('title', flat=True)
    content = BookContent.objects.values_list('content', flat=True)

    # print(title[0])
    # print(content[0])

    # save to dbase
    # r = BookContent(title=title, content=content)
    # r.save()

    context ={
        'id': id,
        'titles': title,
        'contents': content,
    }
    return render(request, 'home2.html', context)

