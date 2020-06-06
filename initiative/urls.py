from django.urls import path

from initiative.views import *

urlpatterns = [
    path('categories/', HeadingCategoriesListView.as_view()),
    path('all_categories/', AllCategoriesListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('initiative/', InitiativeListView.as_view()),
    path('initiative/<int:pk>/', InitiativeDetailView.as_view()),
    path('user_initiative/', InitiativeListViewByUser.as_view()),

    # path('geo/', GeoAPIView.as_view()),
]