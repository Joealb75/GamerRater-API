from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2500)
    designer = models.CharField(max_length=200)
    yearReleased = models.CharField(max_length=30)
    numberOfPlayers = models.IntegerField()
    timeToPlay = models.CharField(max_length=200)
    ageRating = models.CharField(max_length=200)
    averageRating = models.CharField(max_length=200)
    category = models.ManyToManyField(
        "Category",
        through = "GameCategory",
        related_name="games"
    )