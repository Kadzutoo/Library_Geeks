from django.urls import path
from .views import AboutMeView, AboutMyPetView, CurrentTimeView, BookListView, BookDetailView, SearchView

urlpatterns = [
    path('about_me/', AboutMeView.as_view(), name='about_me'),
    path('about_my_pet/', AboutMyPetView.as_view(), name='about_my_pet'),
    path('current_time/', CurrentTimeView.as_view(), name='current_time'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchView.as_view(), name='search'),
]
