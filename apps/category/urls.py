from django.urls import path

from .views import ListCategoryView, CategoryDetailView

urlpatterns = [
    path('category/', ListCategoryView.as_view(), name='categories'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category')
]
