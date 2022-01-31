from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import LaneSerializer, UserSerializer

class UserCreateApiView(APIView):
  def post(self, request):
    user_data = {
      'user_id': request.data.get('user_id'),
      'name': request.data.get('name'),
      'email': request.data.get('email')
    }
    serializer = UserSerializer(data=user_data)
    if serializer.is_valid():
      serializer.save()
      default_lanes = [
        {
          'name': 'To-Do',
          'description': 'To Do List',
          'user_id': request.data.get('user_id')
        },
        {
          'name': 'In Progress',
          'description': 'In Progress task',
          'user_id': request.data.get('user_id')
        },
        {
          'name': 'Completed',
          'description': 'Completed tasks',
          'user_id': request.data.get('user_id')
        }
      ]
      for lane in default_lanes:
        lane_serializer = LaneSerializer(data=lane)
        if lane_serializer.is_valid():
          lane_serializer.save()
        else:
          return Response(lane_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)