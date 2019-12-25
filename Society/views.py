from django.shortcuts import render
from Society.models import Society
from Society.serializer import serializers
from rest_framework import generics
# Create your views here.


class SocietyList(generics.ListCreateAPIView):
    queryset = Society.objects.all()
    serializer_class = serializers


class SocietyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = serializers
