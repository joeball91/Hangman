from django.db import models

# Create your models here.


class Game(models.Model):

    ANIMALS = 'ANIMALS'
    CITIES = 'CITIES'
    MOVIES = 'MOVIES'
    CATEGORY_CHOICES = [
        (ANIMALS, 'Animals'),
        (CITIES, 'Cities'),
        (MOVIES, 'Movies'),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=ANIMALS,
    )
    answer = models.CharField(max_length=20)
    guess = models.CharField(max_length=1)
    hangman_body = models.ImageField()
    is_game_over = models.BooleanField(default=False)
