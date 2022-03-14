from django.db import models

# Create your models here.


class Game(models.Model):
    category = models.CharField(max_length=20)
    answer = models.CharField(max_length=20)
    guess = models.CharField(max_length=1)
    hangman_body = models.CharField(max_length=200)
    is_game_over = models.BooleanField(default=False)
