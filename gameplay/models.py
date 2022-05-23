from django.db import models

# Create your models here.


class Game(models.Model):

    ANIMALS = 'Animals'
    CITIES = 'Cities'
    FAMOUS = 'Famous'
    CATEGORY_CHOICES = [
        (ANIMALS, 'Animals'),
        (CITIES, 'Cities'),
        (FAMOUS, 'Famous'),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
    )
    game_id = models.AutoField(primary_key=True, default=0)
    answer = models.CharField(max_length=20)
    guess = models.CharField(max_length=1)
    letters = models.CharField(max_length=100, default="")
    letters_guessed = models.CharField(max_length=20, default="")
    hangman_body = models.ImageField(default="")
    status = models.CharField(max_length=10, default="")
    display1 = models.CharField(max_length=20)
    display2 = models.CharField(max_length=20, default="")
    count = models.IntegerField(default=1)
