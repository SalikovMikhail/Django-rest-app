from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.filters import SearchFilter


from .serializers import ListCategorySerializers
from .models import Category


class ListCategoryView(ListCreateAPIView):
    """Отдает список категорий или создает категорию"""
    queryset = Category.objects.all()
    serializer_class = ListCategorySerializers
    filter_backends = [SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        return serializer.save()


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    """Отдает, обновляет, удаляет категорию по id"""
    queryset = Category.objects.all()
    serializer_class = ListCategorySerializers
