from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
    """docstring for BlogListView"""
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    """docstring for BlogDetailView"""
    model = Post
    template_name = 'post_detail.html'
