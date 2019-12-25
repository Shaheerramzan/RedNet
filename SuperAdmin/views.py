from rest_framework import generics

from SuperAdmin.models import SuperAdmin
from SuperAdmin.serializer import serializers


# Create your views here.


class SuperAdminAdminList(generics.ListCreateAPIView):
    queryset = SuperAdmin.objects.all()
    serializer_class = serializers


class SuperAdminAdminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SuperAdmin.objects.all()
    serializer_class = serializers
