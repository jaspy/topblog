from django.db import models

# Create your models here.
class Post(models.Model):
    """
    docstring
    """
    title = models.CharField(max_length=100, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    content = models.TextField()
    author = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    docstring
    """
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.CharField(max_length=100, db_index=True)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.author
