from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Lane
from ..serializers import LaneSerializer

class LaneListApiView(APIView):
  def get(self, request):
    if 'name' in request.query_params:
      lanes = Lane.objects.filter(
        name__in=request.query_params.getlist('name')
      )
    else:
      lanes = Lane.objects.all()
    serializer = LaneSerializer(lanes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    data = {
      'name': request.data.get('name'),
      'description': request.data.get('description')
    }
    serializer = LaneSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)