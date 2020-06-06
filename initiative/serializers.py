from rest_framework import serializers

from initiative.models import Category, InitiativePhoto, Initiative


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


class InitiativePhotoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = InitiativePhoto
        fields = '__all__'


class InitiativeCreateSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        photos_fields = kwargs.pop('photos', None)
        super().__init__(*args, **kwargs)
        if photos_fields:
            # да file field хотя должен быть image field, ругается на png, не хочу искать настройки
            # TODO переделать потом на ImageField
            field_update_dict = {field: serializers.FileField(required=False, write_only=True) for field in
                                 photos_fields}
            self.fields.update(**field_update_dict)

    def create(self, validated_data):
        from django.core.files.uploadedfile import InMemoryUploadedFile
        validated_data_copy = validated_data.copy()
        validated_files = []
        for key, value in validated_data_copy.items():
            if isinstance(value, InMemoryUploadedFile):
                validated_files.append(value)
                validated_data.pop(key)
        initiative = super().create(validated_data)
        for file in validated_files:
            InitiativePhoto.objects.create(initiative=initiative, photo=file)
        return initiative

    class Meta:
        model = Initiative
        fields = ['initiative_text', 'leader', 'category', 'initiative_type']
