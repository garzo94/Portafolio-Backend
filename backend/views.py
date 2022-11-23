from django.shortcuts import render
from backend.models import DataCard
from rest_framework import viewsets
from rest_framework import permissions
from backend.serializers import DataCardSerializer
# Create your views here.

class DataCardViewSet(viewsets.ModelViewSet):
    queryset = DataCard.objects.all()
    serializer_class = DataCardSerializer
    # permission_classes = [permissions.IsAdminUser]
