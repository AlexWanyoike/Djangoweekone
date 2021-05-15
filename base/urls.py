from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^base', views.base, name='base'),
    url(r'^viewphoto', views.viewphoto, name='viewphoto'),
    url(r'^create', views.create, name='create'),
]