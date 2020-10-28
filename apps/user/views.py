from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter

from .models import User
from .serializers import UserListSerializer


class ListUserView(ListCreateAPIView):
    """Отдает список пользователей, создает пользователя"""
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name']


class UserDetailView(RetrieveUpdateDestroyAPIView):
    """Отдает, обновляет, удаляет пользователя по id"""
    queryset = User.objects.all()
    serializer_class = UserListSerializer
