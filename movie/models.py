from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=30, blank=True)
    Title = models.CharField(max_length=60, blank=True)
    Year = models.CharField(max_length=60, blank=True)
    Type = models.CharField(max_length=60, blank=True)
    Poster = models.CharField(max_length=1000, blank=True)
    slug = models.SlugField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={
            'slug': self.slug
        })


class Comment(models.Model):
    body = models.TextField(max_length=100)
