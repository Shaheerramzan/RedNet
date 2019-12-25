from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from ReportProblem.models import Report
from ReportProblem.serializer import ReportSerializer
from rest_framework import generics
# Create your views here.


class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportRetrieveView(APIView):
    def get(self, request, pk, *args, **kwargs):
        report = Report.objects.get(id=pk)
        reports_data = ReportSerializer(report)
        return Response(reports_data.data)