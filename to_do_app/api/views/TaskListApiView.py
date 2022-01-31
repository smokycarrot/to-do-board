from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Task
from ..serializers import TaskSerializer

# Create your views here.
class TaskListApiView(APIView):
  def get(self, request):
    if 'user_id' in request.query_params:
      tasks = Task.objects.filter(
        user__in=request.query_params.getlist('user_id')
      )
    else:
      tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    

  def post(self, request):
    data = {
      'user_id': request.data.get('user_id'),
      'notes': request.data.get('notes'),
      'summary': request.data.get('summary')
    }
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)