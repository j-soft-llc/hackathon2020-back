from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import LeaderSerializer, ProfileUpdateSerializer, ProfileReadSerializer


class LeadersListView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = LeaderSerializer

    def get_queryset(self):
        qs = self.queryset.filter(district__isnull=False).exclude(сompetencies=None)\
            .prefetch_related('district', 'сompetencies')
        return qs


class LeadersDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = LeaderSerializer

    def get_queryset(self):
        qs = self.queryset.filter(district__isnull=False).exclude(сompetencies=None) \
            .prefetch_related('district', 'сompetencies')
        return qs


class ProfileApiView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileUpdateSerializer

    def get_object(self):
        return get_object_or_404(self.queryset, **{'pk': self.request.user.pk})

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProfileReadSerializer
        else:
            return self.serializer_class

    def get_queryset(self):
        return self.queryset.filter(pk=self.request.user.id)
