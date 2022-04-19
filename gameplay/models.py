from django.db import models

# Create your models here.


class Game(models.Model):

    ANIMALS = 'ANIMALS'
    CITIES = 'CITIES'
    FAMOUS = 'FAMOUS'
    CATEGORY_CHOICES = [
        (ANIMALS, 'Animals'),
        (CITIES, 'Cities'),
        (FAMOUS, 'Famous'),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=ANIMALS,
    )
    answer = models.CharField(max_length=20)
    guess = models.CharField(max_length=1)
    letters = models.CharField(max_length=100, default="")
    letters_guessed = models.CharField(max_length=20, default="")
    hangman_body = models.ImageField()
    is_game_over = models.BooleanField(default=False)
    display1 = models.CharField(max_length=20, default="")
    display2 = models.CharField(max_length=20, default="")
