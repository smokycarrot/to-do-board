from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Lane
from ..serializers import LaneSerializer


class LaneDetailApiView(APIView):
  def get_object(self, lane_id):
    try:
      return Lane.objects.get(id=lane_id)
    except Lane.DoesNotExist:
      return None
  
  def get(self, request, lane_id):
    lane_instance = self.get_object(lane_id)
    if not lane_instance:
      return Response({"response": "Task with given lane id does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    serializer = LaneSerializer(lane_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def put(self, request, lane_id):
    lane_instance = self.get_object(lane_id)
    if not lane_instance:
      return Response(
        {"response": "Lane with given id does not exist"},
        status=status.HTTP_400_BAD_REQUEST)
    data = {
      'name': request.data.get('name'),
      'description': request.data.get('description')
    }
    serializer = LaneSerializer(instance=lane_instance, data=data, partial = True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, lane_id):
    task_instance = self.get_object(lane_id)
    if not task_instance:
      return Response(
        {"response": "Lane with given id does not exist"},
        status=status.HTTP_400_BAD_REQUEST
      )
    task_instance.delete()
    return Response(
      {"response": "Object deleted!"},
      status=status.HTTP_200_OK
    )
