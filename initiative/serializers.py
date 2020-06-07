from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from initiative.models import Category, Initiative, InitiativePhoto


class SimpleCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class FullCategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        result = []
        for child in obj.children_categories.all():
            result.append(
                {
                    'id': child.id,
                    'name': child.name,
                }
            )
        return result

    class Meta:
        model = Category
        fields = ['id', 'name', 'children']


class InitiativePhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = InitiativePhoto
        fields = ['photo']


class InitiativeSerializer(serializers.ModelSerializer):

    photo = InitiativePhotoSerializer(many=True)

    class Meta:
        model = Initiative
        fields = ['id', 'initiative_text', 'leader', 'category', 'initiative_type', 'owner', 'photo']
