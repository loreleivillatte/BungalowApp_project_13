from django.db.models import Count
from guest.models import Favorite, List


def top_name(num):
    items = Favorite.objects.filter(top_id=num).values('list__name').annotate(c=Count('list__name')) \
        .exclude(list__name__exact='').order_by('-c')[:5]

    return items


def top_author(num):
    items = Favorite.objects.filter(top_id=num).values('list__author') \
        .annotate(c=Count('list__author')).exclude(list__author__exact='').order_by('-c')[:5]
    return items
