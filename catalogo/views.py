from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.http import Http404
from django. shortcuts import redirect, render
from .models import Book
# Create your views here.
def index(request):  
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()

    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  
    
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )
class BookListView(generic.ListView):
    model = Book
    
 
class BookDetailView(generic.DetailView):
    model = Book
    
    
def get_queryset(self):
    return Book.objects.filter(title__icontains='war')[:5]
    
def get_context_data(self, **kwargs):
    context = super(BookListView, self).get_context_data(**kwargs)
    context['some_data'] = 'This is just some data'
    return context

def book_detail_view(request,pk):
    try:book_id=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
        book_id=get_object_or_404(Book, pk=pk)
    return render(
    request,
    'catalogo/book_detail.html',
    context={'book':book_id,}
    )
