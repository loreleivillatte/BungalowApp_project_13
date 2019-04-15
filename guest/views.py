from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Favorite, Post, UserMood, List, Top, Dash, Mood, Choice, Topic, Message
from .forms_choice import NewSentenceForm, NewFavoriteForm


def index(request):
    if request.user.is_authenticated:
        top_list = Top.objects.order_by('pk')
        dash = Dash.objects.get(pk=1)
        participated = Post.objects.filter(user_id=request.user.id).exists()
        post = Post.objects.all()
        moods = Mood.objects.all()
        u_mood = UserMood.objects.filter(user_id=request.user.id).values('mood__number').first()
        # u = u_mood['mood__number']
        if u_mood is None:
            u = int(0)
        else:
            u = u_mood['mood__number']
        message_received = Message.objects.filter(receiver_id=request.user.id).last()
        topic = Topic.objects.last()
        if topic is not None:
            participated_topic = Choice.objects.filter(user_id=request.user, topic_id=topic.id)
        return render(request, 'guest/index.html', locals())
    else:
        return render(request, 'guest/authenticate.html')


@login_required
def save_vote(request, topic_id, slug):
    vote = Choice.objects.create(user_id=request.user.id, topic_id=topic_id, submit=slug)
    messages.success(request, 'Done')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), locals())


@login_required
def save_mood(request, mood_id):
    mood, created = UserMood.objects.update_or_create(user_id=request.user.id, defaults={'mood_id': mood_id})
    messages.success(request, 'Done')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), locals())


@login_required
def new_sentence(request, dash_id):
    list_sentence = Post.objects.all()
    if request.method == 'POST':
        form = NewSentenceForm(request.POST)
        if form.is_valid():
            Post.objects.create(sentence=form.cleaned_data.get('sentence'), user_id=request.user.id, dash_id=1)
            messages.success(request, 'Done')
            return redirect('index')
    else:
        form = NewSentenceForm()
    return render(request, 'guest/dash.html', locals())


@login_required
def new_favorite(request, top_id):
    list_item = Favorite.objects.filter(user_id=request.user, top_id=top_id).values('list__name', 'list__author')\
        .order_by('-id')
    top = Top.objects.get(pk=top_id)
    if request.method == 'POST':
        form = NewFavoriteForm(request.POST)
        if form.is_valid():
            """item, created = List.objects.get_or_create(author=form.cleaned_data.get('author'),
                                                       name=form.cleaned_data.get('name'), top_id=top_id)"""
            item, created = List.objects.get_or_create(author=form.cleaned_data.get('author'),
                                                       name=form.cleaned_data.get('name'), top_id=top_id)
            Favorite.objects.update_or_create(user_id=request.user.id, list_id=item.id, top_id=top_id)
            messages.success(request, 'Done')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = NewFavoriteForm()
    return render(request, 'guest/items.html', locals())



