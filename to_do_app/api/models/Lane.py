from django.db import models
from .User import User

class Lane(models.Model):
  name = models.CharField(max_length=40)
  description = models.TextField()
  user_id = models.ForeignKey(User, to_field='user_id', on_delete=models.CASCADE)

  def __str__(self):
    return self.name