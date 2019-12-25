from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

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


class DonorRetrieveView(APIView):
    def get(self, request, pk, *args, **kwargs):
        donor = Donor.objects.get(id=pk)
        donors_data = serializers(donor)
        return Response(donors_data.data)