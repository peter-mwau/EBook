from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home, name="home"),
    path('', views.upload_document, name="doc"),
    path('upload/', views.upload_document, name='upload_document'),
]
