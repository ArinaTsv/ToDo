from django.shortcuts import render, HttpResponse
from .models import ToDo, Books

def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todos": todo_list})

def books(request):
    book_list = Books.objects.all()
    return render(request, "books.html", {"books": book_list})