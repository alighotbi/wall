from rest_framework import status

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer
from .permissions import IsUser

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return  Response (serializer.data, status=status.HTTP_200_OK)
