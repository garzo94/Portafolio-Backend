from django.shortcuts import render
from backend.models import DataCard
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.serializers import DataCardSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class DataCardApiView(APIView,PageNumberPagination):
    def get(self,request,type="all"):

        if type == 'all':
            queryset = DataCard.objects.all()
            results = self.paginate_queryset(queryset,request,view=self)
            serializer = DataCardSerializer(results, many=True)
            return self.get_paginated_response(serializer.data)

        else:
            queryset = DataCard.objects.filter(appType=type)
            serializer = DataCardSerializer(queryset, many=True)
            return Response(serializer.data)

        # permission_classes = [permissions.IsAdminUser]