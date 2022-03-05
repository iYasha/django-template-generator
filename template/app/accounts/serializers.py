from rest_framework import serializers

from accounts.models import *

class ErrorSerializer(serializers.Serializer):  # noqa
    detail = serializers.CharField(max_length=255)
