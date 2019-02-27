from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts


class PostListView(ListView):
    model = Posts
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 4
