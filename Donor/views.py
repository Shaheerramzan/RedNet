from django.shortcuts import render
from Donor.models import Donor
from Donor.serializer import serializers
# Create your views here.

from rest_framework import generics


class DonorList(generics.ListCreateAPIView):
    queryset = Donor.objects.all()
    serializer_class = serializers


class DonorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donor.objects.all()
    serializer_class = serializers
