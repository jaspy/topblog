from django.db import models

# Create your models here.
class Posts(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    content = models.TextField()
    author = models.CharField(max_length=100, db_index=True)


class Comments(models.Model):
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)
    author = models.CharField(max_length=100, db_index=True)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
