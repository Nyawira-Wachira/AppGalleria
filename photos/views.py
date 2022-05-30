from django.shortcuts import render

import photos
from .models import Category,Image,Location 

# Create your views here.
def gallery(request):
    images = Image.objects.all()
    context = {'images':images}
    return render (request, 'gallery.html',context)

def photo(request):
    image = Image.objects.get()
    return render (request, 'photo.html')