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
    # Start page for Hangman
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
        game.answer = answer
        game.hangman_body = "../static/images/hangman1.png"
        game.category = 'Famous'
        split_word = answer.split()

        first_name = split_word[0]
        last_name = split_word[1]

        game.display1 = list(range(len(first_name)))
        for x in range(len(first_name)):
            game.display1[x] = "_ "
        game.display1 = "".join(game.display1)

        game.display2 = list(range(len(last_name)))
        for x in range(len(last_name)):
            game.display2[x] = "_ "
        game.display2 = "".join(game.display2)

        game.save()

        return render(request, 'index.html', {"game": game})

    else:

        return evaluate_guess(request)


def start_animals_game(request):
    if request.method == 'GET':
        load_animals_dict()
        word = generate_animals_word()
        game = Game(answer=word)
        game.answer = word
        game.hangman_body = "../static/images/hangman1.png"
        game.category = 'Animals'

        for x in range(len(word)):
            game.display1 += '_  '

        game.save()

        return render(request, 'index.html', {"game": game})

    else:

        return evaluate_guess(request)


def start_cities_game(request):
    # serializer = GameSerializer
    if request.method == 'GET':
        load_cities_dict()
        answer = generate_cities_word()
        game = Game(answer=answer)
        game.answer = answer
        game.hangman_body = "../static/images/hangman1.png"
        game.category = 'Cities'
        word = answer.split()

        if len(word) == 2:
            first_part = word[0]
            second_part = word[1]

            game.display1 = list(range(len(first_part)))
            for x in range(len(first_part)):
                game.display1[x] = "_ "
            game.display1 = "".join(game.display1)

            game.display2 = list(range(len(second_part)))
            for x in range(len(second_part)):
                game.display2[x] = "_ "
            game.display2 = "".join(game.display2)

        else:
            first_part = word[0]

            game.display1 = list(range(len(first_part)))
            for x in range(len(first_part)):
                game.display1[x] = "_ "
            game.display1 = "".join(game.display1)

        game.save()

        return render(request, 'index.html', {"game": game})

    else:

        return evaluate_guess(request)


def end_game(game):
    pass


def evaluate_guess(request):
    count = 0
    missed_guess = True
    already_guessed = False
    game_id = int(request.POST['game_id'])
    letter_guess = request.POST['letter']

    game = Game.objects.get(game_id=game_id)
    answer = game.answer.split()
    guessed = list(game.letters_guessed)
    correct = list(game.correct_guesses)
    wrong = list(game.wrong_guesses)

    if letter_guess in game.letters_guessed:
        already_guessed = True
    else:
        if letter_guess in game.answer:
            correct.append(letter_guess)
            game.correct_guesses = "".join(correct)
            game.save()
        else:
            wrong.append(letter_guess)
            game.wrong_guesses = "".join(wrong)
            game.save()
        guessed.append(letter_guess)
        game.letters_guessed = "".join(guessed)
        game.save()
    word1 = ""
    word2 = ""

    if len(answer) == 2:

        for char in answer[0]:
            if char in guessed:
                word1 += char
            else:
                count += 1
                word1 += '_ '
        game.display1 = word1

        for char in answer[1]:
            if char in guessed:
                word2 += char
            else:
                count += 1
                word2 += '_ '
        game.display2 = word2

    else:
        for char in answer[0]:
            if char in guessed:
                word1 += char
            else:
                count += 1
                word1 += '_ '
        game.display1 = word1

    if count == 0:
        game.status = 'win'
        game.hangman_body = "../static/images/hangmanwin.png"
        game.save()

    if len(answer) == 2:

        for char in answer[0]:
            if letter_guess is char:
                missed_guess = False

        for char in answer[1]:
            if letter_guess is char:
                missed_guess = False

    else:
        for char in answer[0]:
            if letter_guess is char:
                missed_guess = False

    if missed_guess:
        if already_guessed:
            game.count = game.count
            game.hangman_body = game.hangman_body
            game.save()
        else:
            game.count += 1
            game.hangman_body = "../static/images/hangman" + str(game.count) + ".png"
            game.save()

        if game.count == 8:
            game.status = 'lose'
            game.save()

    return render(request, 'index.html', {"game": game})

# def ajax_test_view(request):
#     return JsonResponse
