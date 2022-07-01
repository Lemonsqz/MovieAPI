from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('movie_detail/<slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/comment/', AddCommentView.as_view(), name='add_comment'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)