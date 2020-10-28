from django.urls import path
from .views import ListAuthorView, DetailAuthorView

urlpatterns = [
    path('author/', ListAuthorView.as_view(), name='authors'),
    path('author/<int:pk>/', DetailAuthorView.as_view(), name='author_detail')
]
