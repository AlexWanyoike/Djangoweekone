from django.conf import settings
from django.conf.urls.static import static


from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('viewphoto/', views.viewphoto, name='viewphoto'),
    path('create/', views.create, name='create'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)