from rest_framework import serializers
from SuperAdmin.models import SuperAdmin


class SuperAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperAdmin
        fields = '__all__'
