from django.shortcuts import render
from .models import Category,Image,Location 

# Create your views here.


def navbar(request):
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render (request, "navbar.html", {'categories':categories,'locations':locations})

def gallery(request):
    locations = Location.objects.all()
    categories = Category.objects.all()
    images = Image.objects.all()
    return render (request, 'gallery.html', {'images':images,'categories':categories,'locations':locations})


def image(request, image_id): 
    image = Image.objects.get(id=image_id)
    return render (request, "photo.html",{"image":image})

def category(request, category_Id):
    single_category =Category.objects.get(id=category_Id) 
    images = Image.objects.filter(category=single_category)
    return render(request,'categories/category.html',{"images":images, "category":single_category})

def location(request, location_Id):
    single_location =Location.objects.get(id=location_Id) 
    images = Image.objects.filter(location=single_location)
    return render(request,'location/location.html',{"images":images, "location":single_location})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})