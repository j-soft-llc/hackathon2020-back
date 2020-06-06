from django.urls import path

from .views import GeoAPIView

urlpatterns = [
    path('geo/', GeoAPIView.as_view()),
]