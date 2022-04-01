from django.shortcuts import render
from gameplay.models import Game

import random

game_dict = []


def index(request):
    # Home page for Hangman
    return render(request, 'index.html')


def get_choice(request):
    pass


def load_dict():
    pass


def generate_word():
    pass
