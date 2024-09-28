from rest_framework import serializers

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers