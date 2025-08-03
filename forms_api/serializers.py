from rest_framework import serializers
from .models import BogieChecksheet, WheelSpecification

class BogieChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheet
        fields = '__all__'

class WheelSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecification
        fields = '__all__'

class WheelSpecificationGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecification
        fields = '__all__'

class LoginRequestSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()
