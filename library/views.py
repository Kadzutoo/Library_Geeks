from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import Book
import datetime
from django.views.generic import ListView


#serach
class SearchView(ListView):
    template_name = 'books/book.html'  # Corrected template path
    context_object_name = 'books_list'

    def get_queryset(self):
        return Book.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context



class AboutMeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("My name is Argen")

class AboutMyPetView(TemplateView):
    template_name = 'about_my_pet.html'

class CurrentTimeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(datetime.datetime.now())

class BookListView(ListView):
    model = Book
    template_name = 'books/book.html'
    context_object_name = 'books_list'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
