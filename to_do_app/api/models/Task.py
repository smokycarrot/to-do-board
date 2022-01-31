from django.db import models
from .Lane import Lane
from .User import User


class Task(models.Model):
  summary = models.CharField(max_length=40)
  notes = models.TextField()
  user_id = models.ForeignKey(User, to_field='user_id', on_delete=models.CASCADE)
  lane = models.ForeignKey(Lane, to_field='id', null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return self.summary