# Defines URL patterns for gameplay

from django.urls import path

from . import views

app_name = 'gameplay'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('game', views.start_game, name='game')
]
