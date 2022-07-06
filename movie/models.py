from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=30, blank=True)
    Title = models.CharField(max_length=60, blank=True)
    Year = models.CharField(max_length=60, blank=True)
    Type = models.CharField(max_length=60, blank=True)
    Poster = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={
            'pk': self.id
        })


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments', null=True)
    body = models.TextField(max_length=100, blank=True, verbose_name='Комментарий')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '%s - %s' % (self.movie.Title, self.name)

