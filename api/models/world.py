from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class World(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )
  game = models.CharField(max_length=500)
  name = models.CharField(max_length=100)
  setting = models.CharField(max_length=100)
  description = models.TextField()


  def __str__(self):
    # This must return a string
    return f"This world is named '{self.name}'. It has a {self.setting} setting. A description of the world follows: {self.description}"

  def as_dict(self):
    """Returns dictionary version of World models"""
    return {
        'id': self.id,
        'game': self.game,
        'name': self.name,
        'setting': self.setting,
        'description': self.description
    }
