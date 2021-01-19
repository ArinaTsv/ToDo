from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Books

def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todos": todo_list})

def books(request):
    book_list = Books.objects.all()
    return render(request, "books.html", {"books": book_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)    