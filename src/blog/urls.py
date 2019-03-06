from django.urls import path
from .views import PostListView, PostDetailView, CreateCommentView, GetCommentView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('comment-create/<slug>', CreateCommentView.as_view()),
    path('comments-get/<slug>', GetCommentView.as_view()),
]