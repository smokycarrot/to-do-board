from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Task, User
from ..serializers import TaskSerializer

class UserTaskInfoApiView(APIView):
  def get_task_list(self, user_id):
    try:
      return Task.objects.filter(user_id=user_id)
    except Task.DoesNotExist:
      return None

  def check_user_exists(self, user_id):
    try:
      if User.objects.get(user_id=user_id):
        return True
      else:
        return False
    except User.DoesNotExist:
      return False

  def get(self, request, user_id):
    if not self.check_user_exists(user_id):
      return Response(
        {"error": "User does not exist"},
        status=status.HTTP_400_BAD_REQUEST
      )
    
    tasks = self.get_task_list(user_id)
    if not tasks:
      return Response(
        {"error": "User has no tasks yet"},
        status=status.HTTP_400_BAD_REQUEST
      )
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)