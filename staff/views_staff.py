from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.db.models import Count
from .forms import NewMessageForm, NewTopicForm
from guest.models import Post, Favorite, UserMood, Top, Message, Topic, Choice
from .utils import top_items, count_items
from random import choice


@staff_member_required
def index(request):
    """ Home page """
    top_list = Top.objects.order_by('pk')
    # list of records
    top_music, top_books, top_series = top_items(1), top_items(2), top_items(3)
    users = User.objects.all().exclude(is_staff=True).count()
    books, series, music = count_items(1), count_items(2), count_items(3)
    mood = UserMood.objects.all().count()
    moods = UserMood.objects.values('mood__number').annotate(c=Count('mood__number')).order_by('-c')[:1]
    return render(request, 'staff/index_staff.html', locals())


@staff_member_required
def dash(request):
    posts = Post.objects.filter(dash_id=1).values('dash__post__sentence')
    return render(request, 'staff/dash.html', locals())


@staff_member_required
def lists(request, top_id):
    top_list = Top.objects.order_by('pk')
    items = Favorite.objects.filter(top_id=top_id) \
        .values('list__author') \
        .annotate(c=Count('list__author')).exclude(list__author__exact='') \
        .order_by('-c')
    item = Favorite.objects.filter(top_id=top_id) \
        .values('list__name') \
        .annotate(c=Count('list__name')).exclude(list__name__exact='') \
        .order_by('-c')
    if top_id == 3:
        item = Favorite.objects.filter(top_id=3) \
            .values('list__name') \
            .annotate(c=Count('list__name')) \
            .order_by('-c')
    return render(request, 'staff/list.html', locals())


@staff_member_required
def users(request):
    select_user = User.objects.all().exclude(is_staff=True).values('messages_received', 'username', 'id')\
        .order_by('-messages_received')
    return render(request, 'staff/message/users.html', locals())


@staff_member_required
def sent_user(request, user_id):
    speudo = User.objects.filter(pk=user_id)
    print(speudo)
    if request.method == 'POST':
        form = NewMessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(sender_id=request.user.id, receiver_id=user_id,
                                   content=form.cleaned_data.get('content'))
            messages.success(request, 'Done')
            return redirect('index_staff')
    else:
        form = NewMessageForm()
    return render(request, 'staff/message/sent_user.html', locals())


@staff_member_required
def sent_random(request):
    if request.method == 'POST':
        sent_user = User.objects.all().exclude(is_staff=True)
        user = choice(sent_user)
        form = NewMessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(sender_id=request.user.id, receiver_id=user.id,
                                   content=form.cleaned_data.get('content'))
            messages.success(request, 'Done')
            return redirect('index_staff')
    else:
        form = NewMessageForm()
    return render(request, 'staff/message/random_user.html', locals())


@staff_member_required
def new_topic(request):
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            Topic.objects.create(subject=form.cleaned_data.get('subject'), reply_1=form.cleaned_data.get('reply_1'),
                                 reply_2=form.cleaned_data.get('reply_2'))
            messages.success(request, 'Done')
            return redirect('index_staff')
    else:
        form = NewTopicForm()
    return render(request, 'staff/message/new_topic.html', locals())


@staff_member_required
def topics(request):
    topic = Topic.objects.all()
    return render(request, 'staff/message/topic.html', locals())


@staff_member_required
def detail(request, topic_id):
    sub = Choice.objects.filter(topic_id=topic_id)\
        .values('topic__subject', 'topic__reply_1', 'topic__reply_2', 'topic__choice__submit')\
        .annotate(c=Count('topic__choice__submit'))
    empty = Topic.objects.filter(pk=topic_id).values('subject', 'reply_1', 'reply_2')
    return render(request, 'staff/message/detail.html', locals())


@staff_member_required
def logout_view(request):
    """ log a user out -> redirect to a success page """
    logout(request)
    return redirect('index')
