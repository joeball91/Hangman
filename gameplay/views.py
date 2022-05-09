from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from gameplay.models import Game
from django.views.decorators.csrf import csrf_protect
from rest_framework.response import Response
from .serializers import GameSerializer

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


def start_game(request):
    if request.method == 'GET':
        pass


@csrf_protect
def start_famous_game(request):
    if request.method == 'GET':
        load_famous_dict()
        answer = generate_famous_word()
        game = Game(answer=answer)
        game.category = 'Famous'
        split_word = answer.split()
        first_name = split_word[0]
        last_name = split_word[1]

        for x in range(len(first_name)):
            game.display1 += "_ "

        for x in range(len(last_name)):
            game.display2 += "_ "

        return render(request, 'index.html', {"game": game})
    else:
        return button


def start_animals_game(request):
    if request.method == 'GET':
        load_animals_dict()
        word = generate_animals_word()
        game = Game(answer=word)
        game.category = 'Animals'

        for x in range(len(word)):
            game.display1 += '_  '

        return render(request, 'index.html', {"game": game})


def start_cities_game(request):
    # serializer = GameSerializer
    if request.method == 'GET':
        load_cities_dict()
        answer = generate_cities_word()
        # game = Game.objects.all()
        game = Game(answer=answer)
        game.category = 'Cities'
        city = answer.split()

        if len(city) == 2:
            first_part = city[0]
            second_part = city[1]

            for x in range(len(first_part)):
                game.display1 += "_ "

            for x in range(len(second_part)):
                game.display2 += "_ "

        else:
            first_part = city[0]

            for x in range(len(first_part)):
                game.display1 += "_ "

    # return HttpResponse({"game": game})
    return render(request, 'index.html', {"game": game})

# def ajax_test_view(request):
#     return JsonResponse
