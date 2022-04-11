# Defines URL patterns for gameplay

from django.urls import path

from . import views

app_name = 'gameplay'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('famous/', views.start_famous_game, name='game'),
    path('animals/', views.start_animals_game, name='game'),
    path('cities/', views.start_cities_game, name='game'),
]
