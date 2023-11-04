from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'ListPosts.html'  # Provide the path to your template
    context_object_name = 'posts'  # Optional: Set the context variable name
    ordering = ['-publication_date']  # Optional: Set the default ordering of the list

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'  # Provide the path to your template
    context_object_name = 'post'  # Optional: Set the context variable name
