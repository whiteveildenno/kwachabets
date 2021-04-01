from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('', include('bookmakers.urls')),
    path('', include('contacts.urls')),
    path('admin/', admin.site.urls),
    path("ads.txt", RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),
    ),
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
