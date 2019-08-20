from rest_framework import serializers
from app.request.models import Request
from django.contrib.auth.models import User

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Request
        fields = ('name', 'lastname')
        #fields="__all__"