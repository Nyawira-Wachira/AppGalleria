from django.urls import re_path,path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path(r'^$',views.gallery,name='gallery'),
    re_path(r'^photo/(\d+)',views.image,name ='image'),
    re_path(r'^$',views.navbar,name='navbar'),
    path('category/<int:category_Id>',views.category, name='category'),
    path('location/<int:location_Id>',views.location, name='location'),
    re_path(r'^search/', views.search_results, name='search_results')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)