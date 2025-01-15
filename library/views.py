from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import Book


def about_me(request):
    return HttpResponse("My names Argen")

def about_my_pet(request):
    return render(request, 'about_my_pet.html')

def current_time(request):
    return HttpResponse(datetime.datetime.now())

def book_list_view(request):
    if request.method == 'GET':
        books_list = Book.objects.all()
        return render(request, 'books/book.html', {'books_list': books_list})

def book_detail_view(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'books/book_detail.html', {'book': book})