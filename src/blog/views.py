from django.views.generic import ListView, DetailView, View
from django.shortcuts import HttpResponse, render
from django.http import JsonResponse
from .models import Post
from django.templatetags.static import static

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 4


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_default'] = static('images/user.png')
        return context
    

class CreateCommentView(View):
    def post(self, request, slug):
        comment = request.POST.get('comment')
        post = Post.objects.get(slug__iexact=slug)
        post.comment_set.create(author='user123', message=comment)
        response = {
            'author': 'user123',
            'message': comment,
        }
        return JsonResponse(response)


class GetCommentView(View):
    def get(self, request, slug):        
        comments = Post.objects.get(slug__exact=slug).comment_set.all()

        return JsonResponse([i.as_dict() for i in comments], safe=False)
