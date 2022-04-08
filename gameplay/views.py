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
    # with open("hangman/words.txt") as words:
    #     for word in words:
    #         dic.append(word.strip().lower())
    pass


def generate_word():
    pass


def start_game(request):
    #check for category through button click
    #load word from that category
    #generate blanks based on length of word

    #all without refreshing page

    return render(request, 'index.html')
