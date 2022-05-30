from django.shortcuts import render

import photos
from .models import Category,Image,Location 

# Create your views here.
def gallery(request):
    images = Image.objects.all()
    context = {'images':images}
    return render (request, 'gallery.html',context)

def image(request, image_id): 
    image = Image.objects.get(id=image_id)
    return render (request, "photo.html",{"image":image})

   