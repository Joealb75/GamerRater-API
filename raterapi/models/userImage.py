from django.db import models
from django.contrib.auth.models import User
from .game import Game

class UserImage(models.Model):
    image = models.ImageField(upload_to='player_images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

