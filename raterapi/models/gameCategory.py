from django.db import models
from .game import Game
from .category import Category

class GameCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='gameCategory')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='gameCategory')

    