from django.db import models

# Create your models here.
class Posts(models.Model):
    created_at = models.DateTimeField()