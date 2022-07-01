from django.contrib import admin
from .models import Movie, Comment


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'movie', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_field = ('name', 'email', 'body')


admin.site.register(Movie)
admin.site.register(Comment, CommentAdmin)
