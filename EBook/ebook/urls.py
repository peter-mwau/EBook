from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home, name="home"),
    path('', views.upload_document, name="doc"),
    path('upload/', views.upload_document, name='upload_document'),
    path('bookDetail/<int:book_id>', views.book_detail, name='bookDetail'),
    # path('files/<str:file_name>/', views.serve_file, name='serve_file'),
    path('details/',views.get_all_contents_and_documents, name='details')
]
