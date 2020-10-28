from django.urls import path

from .views import ListUserView, UserDetailView

urlpatterns = [
    path('users/', ListUserView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user')
]