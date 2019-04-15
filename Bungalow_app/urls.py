"""Bungalow_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from guest import views, views_account

urlpatterns = [
    path('staff/', include('staff.urls')),
    path('share/', include('share.urls')),
    path('', views.index, name='index'),
    path('save_vote/<int:topic_id><slug:slug>', views.save_vote, name='save_vote'),
    path('save/<int:mood_id>', views.save_mood, name='save'),
    path('dash/<int:dash_id>', views.new_sentence, name='new_sentence'),
    path('items/<int:top_id>', views.new_favorite, name='item'),
    path('login/', views_account.login_view, name='login'),
    path('signup/', views_account.registration, name='signup'),
    path('logout/', views_account.logout_view, name='logout'),
    path('admin/', admin.site.urls),
]
