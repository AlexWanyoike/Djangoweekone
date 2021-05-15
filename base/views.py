#from datetime import db

from django.shortcuts import render
from django.http  import HttpResponse , request , Http404
from .models import Category , Photo

# Create your views here.
def base(request):

    categories = Category.objects.all()
    photo = Photo.objects.all()
    #context = {'categories': categories, 'photos': photos}
    return render(request, 'base/base.html', {'categories' : categories, 'photo': photo})

def viewphoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'base/photo.html', {'photo':photo})

def create(request):
    return render(request , 'base/create.html')
