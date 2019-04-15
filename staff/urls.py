from django.urls import path
from .import views_staff


urlpatterns = [
    path('', views_staff.index, name='index_staff'),
    path('dash/', views_staff.dash, name='dash'),
    path('users/', views_staff.users, name='users'),
    path('list/<int:top_id>/', views_staff.lists, name='list'),
    path('new_topic/', views_staff.new_topic, name='new_topic'),
    path('topics/', views_staff.topics, name='topics'),
    path('detail_topic/<int:topic_id>/', views_staff.detail, name='detail_topic'),
    path('message/random_user/', views_staff.sent_random, name='random_message'),
    path('message/sent_user/<int:user_id>/', views_staff.sent_user, name='sent_user'),
    path('logout/', views_staff.logout_view, name='logout')
]
