from rest_framework import serializers

from initiative.models import Category


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
