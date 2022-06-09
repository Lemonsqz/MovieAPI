from rest_framework import serializers
from .models import Movie
from drf_writable_nested import WritableNestedModelSerializer

class MovieSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Movie
        fields = ('Title', 'Year', 'Type', 'Poster')