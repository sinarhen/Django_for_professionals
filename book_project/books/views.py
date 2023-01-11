# books/views.py
from django.views.generic import ListView, DetailView
from .models import Book

# Create your views here.
class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'  # new
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail_view.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'book'
