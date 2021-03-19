from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Post

class BlogListView(ListView):
    """docstring for BlogListView"""
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    """docstring for BlogDetailView"""
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    """docstring for BlogCreateView"""
    model = Post
    template_name = 'post_new.html'
    fields =['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    """docstring for BlogUpdateView"""
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    """docstring for BlogDeleteView"""
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')



