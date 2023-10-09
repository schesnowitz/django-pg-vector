from django.contrib import admin
from django.urls import path, include
from .views import index, show_collection, create_collection, search_collection, interact_collection 
app_name = "data_set"
urlpatterns = [
    path('', index, name="index"),
    path('create-collection/', create_collection, name="create_collection"),
    
    path('show-collection/<str:uuid>/', show_collection, name="show_collection"),
    path('search-collection/<str:uuid>/', search_collection, name="search_collection"),
    path('interact-collection/<str:uuid>/', interact_collection, name="interact_collection"),

] 