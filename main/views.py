from django.shortcuts import render, HttpResponse
from .models import ToDo

def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    print (todo_list)
    return render(request, "test.html", {"todo_list": todo_list})
