#from datetime import db

from django.shortcuts import render , redirect
from django.http  import HttpResponse , request , Http404
from .models import Category , Photo , Location

# Create your views here.
def base(request):

    location = request.GET.get('location')
    if location == None:
        photo = Photo.objects.all()
    else:
        photo = Photo.objects.filter(location__name=location)
    locations = Location.objects.all()


    category = request.GET.get('category')
    if category == None:
        photo = Photo.objects.all()
    else:
        photo = Photo.objects.filter(category__name=category)
    categories = Category.objects.all()
    
    context = {'categories': categories, 'photo': photo , 'locations': locations}
    return render(request, 'base/base.html', context)

def viewphoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'base/photo.html', {'photo':photo})

def create(request):
    categories = Category.objects.all()
    locations = Location.objects.all()

    context = {'categories': categories, 'locations': locations}
    return render(request , 'base/base.html', context)








   