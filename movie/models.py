from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Movie', kwargs={'slug': self.slug})


class Comment(models.Model):
    body = models.TextField(max_length=100)
