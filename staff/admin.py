from django.contrib import admin
from guest.models import List, Choice, Favorite, Message, Post, Topic, UserMood


admin.site.register(List)
admin.site.register(Choice)
admin.site.register(Favorite)
admin.site.register(Message)
admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(UserMood)


