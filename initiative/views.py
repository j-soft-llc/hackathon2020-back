from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from initiative.models import Category, Geo
from initiative.serializers import FullCategorySerializer, SimpleCategorySerializer, GeoSerializer


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


class GeoAPIView(ListAPIView):
    queryset = Geo.objects.root_nodes()
    serializer_class = GeoSerializer
    permission_classes = (IsAuthenticated,)
