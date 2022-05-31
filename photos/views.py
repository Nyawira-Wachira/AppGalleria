from django.shortcuts import render
from .models import Category,Image,Location 

# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    # context = {'images':images}
    return render (request, 'gallery.html', {'categories':categories,'images':images})

# def navbar(request):
#     categories = Category.objects.all()
#     print(categories)
#     return render (request, "navbar.html", {'categories':categories})

def image(request, image_id): 
    image = Image.objects.get(id=image_id)
    return render (request, "photo.html",{"image":image})

def category(request, category_Id):
    single_category =Category.objects.get(id=category_Id) 
    images = Image.objects.filter(category=single_category)
    return render(request,'categories/category.html',{"images":images, "category":single_category})