from django.contrib import admin
from django.urls import path, include
from ebook.views import *
from theme.views import change_theme
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('switch-theme/', change_theme, name="change-theme"),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include("ebook.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
