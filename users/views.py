from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import LeaderSerializer


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
