from django.shortcuts import render
from SocietyAdmin.models import SocietyAdmin
from SocietyAdmin.serializer import serializers
from rest_framework import generics
# Create your views here.


class SocietyAdminList(generics.ListCreateAPIView):
    queryset = SocietyAdmin.objects.all()
    serializer_class = serializers


class SocietyAdminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocietyAdmin.objects.all()
    serializer_class = serializers
