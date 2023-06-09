from django.contrib import admin
from django.urls import path, include
from ebook.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('switch-theme/', change_theme, name="change-theme"),
    path('', include("ebook.urls")),
]
