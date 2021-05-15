#from datetime import db

from django.shortcuts import render
from django.http  import HttpResponse , request , Http404


# Create your views here.
def base(request):
    return render(request, 'base/base.html')

def viewphoto(request):
    return render(request, 'base/photo.html')

def create(request):
    return render(request , 'base/create.html')
