from rest_framework import serializers
from ..models import Task, Lane, User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['user_id', 'name', 'email']