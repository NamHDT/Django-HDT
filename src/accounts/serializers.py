from rest_framework import serializers
from .models import Accounts
from django.contrib.auth.models import User

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'