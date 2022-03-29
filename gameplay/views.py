from django.shortcuts import render
import random

game_dict = []


def index(request):
    # Home page for Hangman
    return render(request, 'index.html')


def load_dict():
    pass


def generate_word():
    pass
