from django.db import models
from django.contrib.auth.models import User


class Top(models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class List(models.Model):
    author = models.CharField(max_length=60, blank=True)
    name = models.CharField(max_length=60, blank=True)
    top = models.ForeignKey(Top, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Dash (models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    dash = models.ForeignKey(Dash, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sentence = models.CharField(max_length=60)


class Topic (models.Model):
    subject = models.CharField(max_length=200)
    reply_1 = models.CharField(max_length=30)
    reply_2 = models.CharField(max_length=30)
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Choice(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submit = models.CharField(max_length=30)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    top = models.ForeignKey(Top, on_delete=models.CASCADE, null=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE)


class Mood(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return self.number


class UserMood(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='messages_sent', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='messages_received', on_delete=models.CASCADE)
    content = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)


"""
class Messages(models.Model):
    sender = models.ForeignKey(User, related_name='messages_sent', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='messages_received', on_delete=models.CASCADE)
    content = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
"""