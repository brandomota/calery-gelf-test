from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from model.models import Object
from model.serializers import ObjectSerializer


class ObjectViewSet(ModelViewSet):
    serializer_class = ObjectSerializer
    queryset = Object.objects.all()