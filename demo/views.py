from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
# Create your views here.


def first(request):
    books = Book.objects.all()
    return render(request, "first_temp.html", {'books': books})