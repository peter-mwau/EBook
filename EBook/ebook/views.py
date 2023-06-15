from django.shortcuts import render
import requests
from .models import BookContent
# import redirect
from django.shortcuts import redirect, HttpResponseRedirect


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
        'is_dark_theme': request.session.get('is_dark_theme', False),
    }
    return render(request, 'home2.html', context)


def change_theme(request, **kwargs):
    if 'is_dark_theme' in request.session:
        request.session['is_dark_theme'] = not request.session['is_dark_theme']
    else:
        request.session['is_dark_theme'] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))





