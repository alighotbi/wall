from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

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
    
    
class AdCreateView(APIView):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    
    def post(self, request):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['publisher'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class AdDetailView(APIView):
    serializer_class = AdSerializer
    
    def get(self, request, pk):
        ad = Ad.objects.get(id=pk)
        serializer = AdSerializer(ad)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class AdModifyView(APIView):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    
    def put(self, request, pk):
        ad = Ad.objects.get(publisher=request.user, id=pk)
        serializer = AdSerializer(ad, data=request.data ,partial=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        ad = Ad.objects.get(publisher=request.user, id=pk)
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class AdSearchView(APIView, StandardPagination):
    
    def get(self, request):
        q = request.GET.get('q')
        queryset = Ad.objects.filter(Q(title=q) | Q(caption=q))
        result = self.paginate_queryset(queryset, request)
        serializer = AdSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)