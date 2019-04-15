from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from guest.models import Favorite, Post, UserMood, List, Top, Dash, Mood, Choice, Topic, Message
import json
from django.core.serializers.json import DjangoJSONEncoder
from .utils import top_author, top_name


@staff_member_required
def index_share(request):
    # general mood
    moods = UserMood.objects.values('mood__number').annotate(c=Count('mood__number')) \
        .order_by('-c', '-mood__number').first()
    if moods is None:
        m = int(0)
    else:
        m = moods['mood__number']
    # top five
    music_a, music_n = top_author(1), top_name(1)
    book_a, book_n = top_author(2), top_name(2)
    serie_n = top_name(3)
    # question
    top = Topic.objects.last()
    if top is not None:
        top_val = Topic.objects.filter(pk=top.id).values('subject', 'reply_1', 'reply_2')
        reply_count = Choice.objects.filter(topic_id=top.id).values('topic__subject', 'topic__choice__submit')\
            .annotate(c=Count('topic__choice__submit')).order_by('-c')[:1]
    return render(request, 'share/dash_share.html', locals())


@staff_member_required
def skull(request):
    moods = UserMood.objects.values('mood__number').annotate(c=Count('mood__number')) \
        .order_by('-c', '-mood__number').first()
    m = moods['mood__number']
    posts = Post.objects.values('sentence')
    return render(request, 'share/skull.html', locals())


@staff_member_required
def logout_view(request):
    """ log a user out -> redirect to a success page """
    logout(request)
    return redirect('index')
