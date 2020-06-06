from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from geo.models import Geo


class GeoSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        depth = 1
        model = Geo
        fields = ('id', 'name', 'children')
