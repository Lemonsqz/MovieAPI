from django.contrib import admin
from .models import Movie, Comment, UserMovieRating, RatingStar


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'movie', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_field = ('name', 'body')


admin.site.register(Movie)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserMovieRating)
admin.site.register(RatingStar)
