from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from initiative.models import Category, Initiative
from initiative.serializers import *
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