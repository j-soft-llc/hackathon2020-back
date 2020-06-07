import random

from rest_framework import serializers

from users.models import User


class LeaderSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()
    сompetencies = serializers.SerializerMethodField()

    def get_сompetencies(self, obj):
        result = []
        if obj.сompetencies:
            for comp in obj.сompetencies.all():
                result.append({
                    'id': comp.id,
                    'name': comp.name,
                    'vote_count': random.randint(1, 200)  # TODO голоса фейк
                })
        return result

    def get_location(self, obj):
        location_data = {}
        if obj.district:
            location_data['name'] = obj.district.name
            location_data['lat'] = obj.district.lat
            location_data['long'] = obj.district.long
        return location_data

    class Meta:
        model = User
        fields = ['сompetencies', 'location', 'avatar_link', 'first_name', 'middle_name', 'second_name', 'age',
                  'profession', 'vk_id', 'id']


class ProfileReadSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()

    def get_location(self, obj):
        location_data = {}
        if obj.district:
            location_data['name'] = obj.district.name
            location_data['lat'] = obj.district.lat
            location_data['long'] = obj.district.long
        return location_data

    class Meta:
        model = User
        fields = ['сompetencies', 'avatar_link', 'first_name', 'middle_name', 'second_name', 'age',
                  'profession', 'vk_id', 'profession', 'address', 'location']


class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['сompetencies', 'avatar_link', 'first_name', 'middle_name', 'second_name', 'age',
                  'profession', 'vk_id', 'profession', 'address']