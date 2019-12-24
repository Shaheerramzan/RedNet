from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from library.models import Book


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
