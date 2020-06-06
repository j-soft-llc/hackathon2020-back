from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Geo
from .serializers import GeoSerializer


class GeoAPIView(ListAPIView):
    queryset = Geo.objects.root_nodes()
    serializer_class = GeoSerializer
    permission_classes = (IsAuthenticated,)
