from django.urls import path,include
from .views import *


urlpatterns = [
    path('blogs/',GetBlogs.as_view(), name='blogs')
]
