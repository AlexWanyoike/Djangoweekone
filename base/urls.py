from django.conf import settings
from django.conf.urls.static import static


from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^base', views.base, name='base'),
    url(r'^viewphoto', views.viewphoto, name='viewphoto'),
    url(r'^create', views.create, name='create'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)