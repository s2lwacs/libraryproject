from django.shortcuts import render
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min

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
    # Comprehensive dataset of books
    books = [
        Book(title='Continuous Delivery', author='J. Humble and D. Farley', price=120.00, edition=3),
        Book(title='Reversing: Secrets of Reverse Engineering', author='E. Eilam', price=97.00, edition=2),
        Book(title='The Hundred-Page Machine Learning Book', author='Andriy Burkov', price=100.00, edition=4),
        Book(title='Clean Code: A Handbook of Agile Software Craftsmanship', author='Robert C. Martin', price=50.00, edition=2),
        Book(title='Design Patterns: Elements of Reusable Object-Oriented Software', author='Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides', price=75.00, edition=1),
        Book(title='Artificial Intelligence: A Modern Approach', author='Stuart Russell, Peter Norvig', price=150.00, edition=3),
        Book(title='Introduction to Algorithms', author='Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein', price=85.00, edition=4),
        Book(title='The Pragmatic Programmer: Your Journey To Mastery', author='Andrew Hunt, David Thomas', price=65.00, edition=2),
        Book(title='Python Crash Course: A Hands-On Project-Based Introduction to Programming', author='Eric Matthes', price=40.00, edition=1),
        Book(title='You Don’t Know JS Yet: Scope & Closures', author='Kyle Simpson', price=30.00, edition=1),
        Book(title='Deep Learning with Python', author='Francois Chollet', price=95.00, edition=2),
        Book(title='Cracking the Coding Interview: 189 Programming Questions and Solutions', author='Gayle Laakmann McDowell', price=45.00, edition=6)
    ]

    # Save all books to the database
    for book in books:
        book.save()

    return HttpResponse("Books have been inserted successfully!")

def simple_query(request):
    # Retrieve all books where the title contains "and" (case-insensitive)
   mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
   print(mybooks)
   return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def lookup_query(request):
    mybooks=books=Book.objects.filter(author__isnull =False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def task1(request):
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'bookmodule/task1.html', {'books': books})

def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=2) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task3.html', {'books': books})

def task4(request):
    books = Book.objects.all().order_by('title')  # Order books by title
    return render(request, 'bookmodule/task4.html', {'books': books})

def task5(request):
    aggregation = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'aggregation': aggregation}) 
    
def list_books_crud(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part1_listbooks.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        # Get form data from POST request
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')

        # Create a new book object and save it
        new_book = Book(title=title, author=author, price=price, edition=edition)
        new_book.save()
        
        books = Book.objects.all()

        return list_books_crud(request)

    # If GET request, render the add book form
    return render(request, 'bookmodule/lab9_part1_addbook.html')
    
def edit_book(request, book_id):
    return HttpResponse(f"Edit Book functionality for book ID {book_id} goes here.")

def delete_book(request, book_id):
    return HttpResponse(f"Delete Book functionality for book ID {book_id} goes here.")


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