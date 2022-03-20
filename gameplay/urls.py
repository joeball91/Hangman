# Defines URL patterns for gameplay

from django.urls import path, include

from . import views

app_name = 'gameplay'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
]
