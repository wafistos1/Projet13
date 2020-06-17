from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import search, filter_search, search_categorie


urlpatterns = [
     path('search/', search, name='search'),
     path('search/filter/', filter_search, name='filter'),
     path('search/categorie/<search>', search_categorie, name='search_categorie'),

]

