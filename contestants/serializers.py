from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import RegistrationPurchase

class RegPurchaseSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=False, required=True)
    phonenumber = serializers.CharField(max_length=15,allow_blank=False,required=True)
    class Meta:
        model = RegistrationPurchase
        fields = ["id","email","phonenumber","ref"]

        read_only_fields = ["id","ref"]

class VerifyTransSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationPurchase
        fields = ["ref","verified"]