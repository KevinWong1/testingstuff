from django.db import models

# Create your models here.

class Blog(models.Model):
    # CharField refers to text
    name = models.CharField(max_length=127)
    time = models.CharField(max_length=127)
    date = models.CharField(max_length=127)
    post = models.CharField(max_length=127)
