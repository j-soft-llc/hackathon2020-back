from django.urls import path

from users.views import LeadersListView, LeadersDetailView, ProfileApiView

urlpatterns = [
    path('', LeadersListView.as_view()),
    path('my_profile/', ProfileApiView.as_view()),
    path('<int:pk>/', LeadersDetailView.as_view()),
]
