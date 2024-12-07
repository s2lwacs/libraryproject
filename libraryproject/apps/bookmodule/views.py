from django.shortcuts import render
from django.http import HttpResponse

from apps.bookmodule.models import Book


# Create your views here.
def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})

    return render(request, 'bookmodule/search.html')
def insert_books(request):
    # Insert data using the Constructor method
    book1 = Book(title='Continuous Delivery', author='J. Humble and D. Farley', price=120.00, edition=3)
    book1.save()

    book2 = Book(title='Reversing: Secrets of Reverse Engineering', author='E. Eilam', price=97.00, edition=2)
    book2.save()

    book3 = Book(title='The Hundred-Page Machine Learning Book', author='Andriy Burkov', price=100.00, edition=4)
    book3.save()

    return HttpResponse("Books have been inserted successfully!")

def simple_query(request):
    # Retrieve all books where the title contains "and" (case-insensitive)
   mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
   print(mybooks)
   return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def index2(request, val1 = 0): 
    return HttpResponse("value1 = "+str(val1))
def viewbook(request, bookId):
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} 
    return render(request, 'bookmodule/show.html', context)

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def links(request):
    return render(request, 'bookmodule/links.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')