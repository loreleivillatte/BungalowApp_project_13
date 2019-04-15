from django.db.models import Count
from django.contrib.auth.models import User
from guest.models import Favorite, List


def count_items(number):
    count = List.objects.filter(top_id=number).count()
    return count


def list_items(number):
    items = Favorite.objects.filter(top_id=number).values('list').annotate(c=Count('list')).order_by('-c')
    return items


def top_items(number):
    items = Favorite.objects.filter(top_id=number).values('list__name').annotate(c=Count('list__name')).order_by('-c')[:5]
    return items
