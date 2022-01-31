from rest_framework import serializers
from ..models import Task, Lane, User

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = ['user_id', 'summary', 'notes', 'lane', 'id']