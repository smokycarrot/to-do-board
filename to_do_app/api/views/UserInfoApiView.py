from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from ..serializers import UserSerializer

class UserInfoApiView(APIView):
  def get_user_obj(self, user_id):
    try:
      return User.objects.get(user_id=user_id)
    except User.DoesNotExist:
      return None

  def get(self, request, user_id):
    user_info = self.get_user_obj(user_id)
    if not user_info:
      return Response(
        {"error": "User does not exist"},
        status=status.HTTP_400_BAD_REQUEST
      )
    serializer = UserSerializer(user_info)
    return Response(serializer.data, status=status.HTTP_200_OK)
