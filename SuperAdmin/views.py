from django.shortcuts import render
from SuperAdmin.models import SuperAdmin
from SuperAdmin.serializer import serializers
from rest_framework import generics
# Create your views here.


class SuperAdminAdminList(generics.ListCreateAPIView):
    queryset = SuperAdmin.objects.all()
    serializer_class = serializers


class SuperAdminAdminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SuperAdmin.objects.all()
    serializer_class = serializers
