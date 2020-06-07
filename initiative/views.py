from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from initiative.models import Category, Initiative
from initiative.serializers import FullCategorySerializer, SimpleCategorySerializer, InitiativeCreateSerializer, \
    InitiativeSerializer
from users.models import User


class AllCategoriesListView(ListAPIView):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = FullCategorySerializer

    def get_queryset(self):
        return self.queryset.select_related('parent')


class HeadingCategoriesListView(ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True)
    permission_classes = (IsAuthenticated,)
    serializer_class = SimpleCategorySerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = FullCategorySerializer


class CreateInitiative(CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (IsAuthenticated, )
    serializer_class = InitiativeCreateSerializer

    def create(self, request, *args, **kwargs):
        photos_fields = []
        # Считаем что все файлы в запросе с префиксом photo_ это фото обращения
        for file_field in request.FILES.keys():
            if 'photo_' in file_field:
                photos_fields.append(file_field)
        serializer = self.get_serializer(data=request.data, photos=photos_fields)

        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class InitiativeListView(ListAPIView):
    queryset = Initiative.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = InitiativeSerializer


class InitiativeListViewByUser(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = InitiativeSerializer

    def get_queryset(self):
        user_id = self.request.GET.get('user_id')
        user = self.request.user
        if user_id:
            user = User.objects.get(id=user_id)
        return Initiative.objects.filter(owner=user)


class InitiativeDetailView(RetrieveAPIView):
    queryset = Initiative.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = InitiativeSerializer
