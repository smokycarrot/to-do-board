from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Lane, User
from ..serializers import LaneSerializer

class UserLaneInfoApiView(APIView):
  def get_lane_list(self, user_id):
    try:
      return Lane.objects.filter(user_id=user_id)
    except Lane.DoesNotExist:
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
    
    lanes = self.get_lane_list(user_id)
    if not lanes:
      return Response(
        {"error": "User has no tasks yet"},
        status=status.HTTP_400_BAD_REQUEST
      )
    serializer = LaneSerializer(lanes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)