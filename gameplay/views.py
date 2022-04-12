from django.shortcuts import render
from datetime import datetime
from gameplay.models import Game

import random

famous_dict = []
animals_dict = []
cities_dict = []


def index(request):
    # Home page for Hangman
    return render(request, 'index.html')


def load_famous_dict():
    if len(famous_dict) == 0:
        with open("gameplay/static/words/famous_people.txt") as words:
            for word in words:
                famous_dict.append(word.strip().lower())


def load_animals_dict():
    if len(animals_dict) == 0:
        with open("gameplay/static/words/animals.txt") as words:
            for word in words:
                animals_dict.append(word.strip().lower())


def load_cities_dict():
    if len(cities_dict) == 0:
        with open("gameplay/static/words/cities.txt") as words:
            for word in words:
                cities_dict.append(word.strip().lower())


def generate_famous_word():
    return random.choice(famous_dict)


def generate_animals_word():
    return random.choice(animals_dict)


def generate_cities_word():
    return random.choice(cities_dict)


def start_famous_game(request):
    if request.method == 'GET':
        load_famous_dict()
        word = generate_famous_word()
        game = Game(answer=word)

        return render(request, 'index.html')


def start_animals_game(request):
    if request.method == 'GET':
        load_animals_dict()
        word = generate_animals_word()
        game = Game(answer=word)

        return render(request, 'index.html')


def start_cities_game(request):
    if request.method == 'GET':
        load_cities_dict()
        word = generate_cities_word()
        game = Game(answer=word)

        return render(request, 'index.html')
