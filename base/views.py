#from datetime import db

from django.shortcuts import render
from django.http  import HttpResponse , request , Http404
from .models import Category , Photo , Location

# Create your views here.
def base(request):

    categories = Category.objects.all()
    photo = Photo.objects.all()
    context = {'categories': categories, 'photo': photo}
    return render(request, 'base/base.html', context)

def viewphoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'base/photo.html', {'photo':photo})

def create(request):
    categories = Category.objects.all()
    locations = Location.objects.all()

    for photo in photos:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                photo=photo,
            )

    return redirect('base')

    context = {'categories': categories, 'locations': locations}
    return render(request , 'base/create.html', context)
