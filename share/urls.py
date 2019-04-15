from django.urls import path
from .import views


urlpatterns = [
    path('', views.index_share, name='index_share'),
    path('skull/', views.skull, name='skull'),
    ]