from rest_framework import serializers
from .models import Rates

class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rates
        fields = '__all__'