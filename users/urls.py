from django.urls import path

from users.views import LeadersListView, LeadersDetailView

urlpatterns = [
    path('', LeadersListView.as_view()),
    path('<int:pk>/', LeadersDetailView.as_view()),
]
