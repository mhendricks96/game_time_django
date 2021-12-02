from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Team(models.Model):
  name = models.CharField(max_length=64)
  league_number = models.IntegerField()
  team_id = models.IntegerField()

  def __str__(self):
    return self.name
