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

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)
        

def add_book(request):
    form = request.POST
    print(form)

    form_title = form['title']
    form_subtitle = form['subtitle']
    form_description = form['description']
    form_price = form['price']
    form_genre = form['genre']
    form_author = form['author']
    form_year = form['year']

    book = Books(
        title=form_title,
        subtitle=form_subtitle,
        description=form_description,
        price=form_price,
        genre=form_genre,
        author=form_author,
        year=form_year
    )
    book.save()
    return redirect(books)
    
def mark_book(request, id):
    book = Books.objects.get(id=id)
    book.is_favorite = True
    book.save()
    return redirect(books)

    
def unmark_book(request, id):
    book = Books.objects.get(id=id)
    book.is_favorite = False
    book.save()   
    return redirect(books)

def delete_book(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect(books)

def book_detail(request, id):
    bookItem = Books.objects.get(id=id)
    return render(request, "books_detail.html", {"book": bookItem})