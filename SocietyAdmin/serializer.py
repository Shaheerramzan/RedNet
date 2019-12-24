from rest_framework import serializers
from SocietyAdmin.models import SocietyAdmin, Complain


class SocietyAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocietyAdmin
        fields = '__all__'


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = '__all__'
