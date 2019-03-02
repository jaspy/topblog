from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time



def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Post(models.Model):
    """
    docstring
    """
    title = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(default='default.jpg', upload_to='post_pics')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    content = models.TextField()
    author = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)
    
    def get_content(self):
        correct_contnt = []
        if len(self.content) < 200:
            return self.content

        for i in range(200,len(self.content)):
            if self.content[i] == '<':
                return self.content[0:i]
            

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
