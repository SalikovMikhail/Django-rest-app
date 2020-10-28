from django.urls import path
from .views import BookView, BookDetailView, BookCreateView, BookUpdateView

urlpatterns = [
    path('books/', BookView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/update/<int:pk>', BookUpdateView.as_view(), name='book_update')
]