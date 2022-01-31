from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Task
from ..serializers import TaskSerializer

class TaskDetailApiView(APIView):
  def get_object(self, task_id):
    try:
      return Task.objects.get(id=task_id)
    except Task.DoesNotExist:
      return None
  
  def get(self, request, task_id):
    task_instance = self.get_object(task_id)
    if not task_instance:
      return Response({"response": "Task with given id does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    serializer = TaskSerializer(task_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def put(self, request, task_id):
    task_instance = self.get_object(task_id)
    if not task_instance:
      return Response(
        {"response": "Task with given id does not exist"},
        status=status.HTTP_400_BAD_REQUEST)
    data = {
      'user_id': request.data.get('user_id'),
      'notes': request.data.get('notes'),
      'summary': request.data.get('summary'),
      'lane': request.data.get('lane')
    }
    serializer = TaskSerializer(instance=task_instance, data=data, partial = True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, task_id):
    task_instance = self.get_object(task_id)
    if not task_instance:
      return Response(
        {"response": "Task with given id does not exist"},
        status=status.HTTP_400_BAD_REQUEST
      )
    task_instance.delete()
    return Response(
      {"response": "Object deleted!"},
      status=status.HTTP_200_OK
    )
