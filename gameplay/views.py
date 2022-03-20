from django.shortcuts import render

# Create your views here.


def index(request):
    # Home page for Hangman
    return render(request, 'index.html')
