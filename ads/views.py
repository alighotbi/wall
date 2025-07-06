from rest_framework import status

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Ad
from .serializers import AdSerializer
from .pagination import StandardPagination

class AdlistView(APIView, StandardPagination):
    # permission_classes = [IsAuthenticated]
    serializer_class = AdSerializer
    
    def get(self, request):
        ads = Ad.objects.filter(is_public=True)
        result = self.paginate_queryset(ads, request)
        serializer = AdSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)