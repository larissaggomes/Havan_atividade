from rest_framework import serializers
from sale import models


class MaritalStatusSerializer(serializers.Serializer):

    class Meta:
        models = models.MaritalStatus
        fields = '__all__'
