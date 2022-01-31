from django.db import models

class User(models.Model):
  user_id = models.CharField(max_length=40, unique=True)
  name = models.TextField()
  email = models.EmailField()

  def __str__(self):
    return f"{self.user_id} - {self.name}"