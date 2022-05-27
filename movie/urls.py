from django.contrib import admin
from django.urls import path
from . import views
from .views import MovieDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('movie/<str:slug>/', MovieDetailView.as_view(), name='movie_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)