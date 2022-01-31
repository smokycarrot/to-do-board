from rest_framework import serializers
from ..models import Lane

class LaneSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lane
    fields = ['name', 'description', 'user_id', 'id']
