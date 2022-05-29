from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^$',views.gallery,name='gallery'),
    re_path(r'^photo/(\d+)',views.photo,name ='photo')

]