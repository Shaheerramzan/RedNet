from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse, HttpRequest

from Donor.models import Donor
from Donor.serializer import DonorSerializer
# Create your views here.

from rest_framework import generics


class DonorList(generics.ListCreateAPIView):
    serializer_class = DonorSerializer
    queryset = Donor.objects.all()


class DonorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DonorSerializer
    queryset = Donor.objects.all()


class DonorRetrieveView(APIView):
    def get(self, request, pk, *args, **kwargs):
        donor = Donor.objects.get(id=pk)
        donors_data = DonorSerializer(donor)
        return Response(donors_data.data)
