from rest_framework import serializers
from .models import DisabledPerson

class DisabledPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisabledPerson
        fields = ['id', 'name', 'disability_type', 'contact', 'latitude', 'longitude']
