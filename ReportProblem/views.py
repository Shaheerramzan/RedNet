from django.shortcuts import render
from ReportProblem.models import Report
from ReportProblem.serializer import serializers
from rest_framework import generics
# Create your views here.


class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = serializers


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = serializers
