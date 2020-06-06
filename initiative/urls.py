from django.urls import path

from initiative.views import AllCategoriesListView, HeadingCategoriesListView, CategoryDetailView

urlpatterns = [
    path('categories/', HeadingCategoriesListView.as_view()),
    path('all_categories/', AllCategoriesListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
]