
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField 

# Create your models here.

class Players(models.Model):
    firstname = models.CharField(max_length=200, default='Unknown')
    lastname = models.CharField(max_length=200, default='Unknown')
    nation = models.CharField(max_length=200, default='Unknown')
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    overall = models.IntegerField(default=0)
    position = models.CharField(max_length=200, default='Unknown')
    speed = models.IntegerField(default=0)
    shooting = models.IntegerField(default=0)
    passing = models.IntegerField(default=0)
    dribbling = models.IntegerField(default=0)
    defending = models.IntegerField(default=0)
    physical = models.IntegerField(default=0)
    gkrating = models.IntegerField(default=0)
    tradevalue = models.FloatField(default=0.0)
    team = models.ForeignKey('Teams',on_delete=models.CASCADE,related_name='players',null=True,blank=True)


class Teams(models.Model):
    name = models.CharField(max_length=200, default='Unknown')
    rating  = models.IntegerField(default=0)
    selected = models.BooleanField(default = False)

class Formations(models.Model):
    team = models.ForeignKey('Teams', on_delete=models.CASCADE, related_name='formations',null=True,blank=True)
    name = models.CharField(max_length=200, default='Default Formation')
    formation_style = models.CharField(max_length=50, default='442')

class FormationPlayer(models.Model):
    formation = models.ForeignKey('Formations', on_delete=models.CASCADE, related_name='formation_players')
    player = models.ForeignKey('Players', on_delete=models.CASCADE)
    role = models.CharField(
        max_length=50,
        choices=[('Starting', 'Starting'), ('Benched', 'Benched')],
        default='Benched'
    )
    position = models.CharField(max_length=50)



class SavedGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="saved_games")
    gamename = models.CharField(max_length=255, blank=True)  # Optional: A name for the saved game
    teams = models.JSONField(default=dict)  # Store structured JSON data
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.gamename}"