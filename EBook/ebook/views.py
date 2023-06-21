from django.shortcuts import render
import requests
from .models import BookContent
# import redirect
from django.shortcuts import redirect, HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import DocumentForm
from .models import Document
# from docx import Document
from docx import Document as DocxDocument
from django.views.decorators.csrf import csrf_protect


# def home(request):
#     content = BookContent.objects.all()
#     # get title from BookContent
#     id = BookContent.objects.values_list('id', flat=True)
#     title = BookContent.objects.values_list('title', flat=True)
#     content = BookContent.objects.values_list('content', flat=True)
    

#     # print(title[0])
#     # print(content[0])

#     # save to dbase
#     # r = BookContent(title=title, content=content)
#     # r.save()

#     context ={
#         'id': id,
#         'titles': title,
#         'contents': content,
#         'is_dark_theme': request.session.get('is_dark_theme', False),
#     }
#     return render(request, 'home2.html', context)


def change_theme(request, **kwargs):
    if 'is_dark_theme' in request.session:
        request.session['is_dark_theme'] = not request.session['is_dark_theme']
    else:
        request.session['is_dark_theme'] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))





def process_document(file_path):
    doc = DocxDocument(file_path)
    document_contents = ""
    for paragraph in doc.paragraphs:
        document_contents += paragraph.text + "\n"
    return document_contents

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = Document(file=request.FILES['file'])
            document.save()
            # Process the document's contents and pass them to the template
            document_contents = process_document(document.file.path)
            return render(request, 'home.html', {'document_contents': document_contents})
    else:
        form = DocumentForm()
    return render(request, 'home.html', {'form': form})





