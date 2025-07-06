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

    
    def put(self, request):
        user = request.user
        serializer = UserSerializer(data = request.data, isinstance=user)
        # if serializer.is_valid(raise_exception=True):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)