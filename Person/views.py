from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Person.models import Person
from Person.serializer import PersonSerializer


class PersonListView(ListCreateAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        persons_queryset = Person.objects.all()
        blood_group_eq = self.request.GET.get('blood_group_eq')
        if blood_group_eq:
            persons_queryset = persons_queryset.filter(blood_group__contains=blood_group_eq)
        return persons_queryset


class PersonDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class CustomUserView(APIView):
    def get(self, request, *args, **kwargs):
        persons = Person.objects.all()
        persons_data = PersonSerializer(persons, many=True)
        return Response(persons_data.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


class CustomUserRetrieveView(APIView):
    def get(self, request, pk, *args, **kwargs):
        person = Person.objects.get(id=pk)
        persons_data = PersonSerializer(person)
        return Response(persons_data.data)