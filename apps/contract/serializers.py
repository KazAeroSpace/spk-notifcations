from rest_framework import serializers
from .models import Contract

# Serializer for the Contract model
class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'  # Or specify the fields if you don't want all fields
