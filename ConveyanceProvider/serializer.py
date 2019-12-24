from rest_framework import serializers
from ConveyanceProvider.models import ConveyanceProvider


class ConveyanceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConveyanceProvider
        fields = '__all__'
