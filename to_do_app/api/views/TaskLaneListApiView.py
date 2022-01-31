from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Task
from ..serializers import TaskSerializer

class TaskLaneListApiView(APIView):
  def get_tasks(self, lane_id):
    try:
      return Task.objects.filter(lane=lane_id)
    except Task.DoesNotExist:
      return None
  
  def get(self, request, lane_id):
    task_list_instance = self.get_tasks(lane_id)
    if not task_list_instance:
      return Response({"response": "Task with given lane id does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    serializer = TaskSerializer(task_list_instance, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)