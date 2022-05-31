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
    locations = Location.objects.all()
    categories = Category.objects.all()
    image = Image.objects.get(id=image_id)
    return render (request, "photo.html",{"image":image ,'categories':categories,'locations':locations})

def category(request, category_Id):
    locations = Location.objects.all()
    categories = Category.objects.all()
    single_category =Category.objects.get(id=category_Id) 
    images = Image.objects.filter(category=single_category)
    return render(request,'categories/category.html',{"images":images, "category":single_category ,'categories':categories,'locations':locations})

def location(request, location_Id):
    locations = Location.objects.all()
    categories = Category.objects.all()
    single_location =Location.objects.get(id=location_Id) 
    images = Image.objects.filter(location=single_location)
    return render(request,'location/location.html',{"images":images, "location":single_location ,'categories':categories,'locations':locations})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        locations = Location.objects.all()
        categories = Category.objects.all()
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images ,'categories':categories,'locations':locations})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})