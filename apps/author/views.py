from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter

from .serializers import ListAuthorSerializers
from .models import Author


class ListAuthorView(ListCreateAPIView):
    """Отдает список авторов, либо создает автора"""
    queryset = Author.objects.all()
    serializer_class = ListAuthorSerializers
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name']

    def perform_create(self, serializer):
        return serializer.save()


class DetailAuthorView(RetrieveUpdateDestroyAPIView):
    """Отдает автора по id, обновляет информацию, либо удалаяет"""
    queryset = Author.objects.all()
    serializer_class = ListAuthorSerializers
