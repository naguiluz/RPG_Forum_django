from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Character(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )
  game = models.CharField(max_length=500)
  name = models.CharField(max_length=100)
  level = models.IntegerField()
  race = models.CharField(max_length=100)
  discipline = models.CharField(max_length=100)
  background = models.CharField(max_length=100)
  description = models.TextField()
  abilities = models.TextField()
  items = models.TextField()
  backstory = models.TextField()


  def __str__(self):
    # This must return a string
    return f"{self.name} is a character for {self.game} campaigns. Currently a level {self.level} character. They are a {self.race} {self.discipline} with the {self.background} background. || A brief description of their appearance: {self.description} || Some key abilities are: {self.abilities} || Some signature weapons and items are: {self.items}. || Their backstory is: {self.backstory}"

  def as_dict(self):
    """Returns dictionary version of Character models"""
    return {
        'id': self.id,
        'game': self.game,
        'name': self.name,
        'level': self.level,
        'race': self.race,
        'discipline': self.discipline,
        'background': self.background,
        'description': self.description,
        'abilities': self.abilities,
        'items:': self.items,
        'backstory': self.backstory

    }
