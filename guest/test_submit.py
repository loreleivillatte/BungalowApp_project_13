from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse
from guest.models import Top, List, Favorite
from guest.views import new_favorite


class NewFavoriteTests(TestCase):
    def setUp(self):
        top = Top.objects.create(question='test')
        user = User.objects.create_user(username='john', email='john@doe.com', password='123')
        new_item = List.objects.create(author='doe', name='john', top_id=top.id)
        Favorite.objects.create(list=new_item, top=top, user=user)
        url = reverse('item', args=['1'])
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 302)

    def test_view_function(self):
        view = resolve('/items/1')
        self.assertEquals(view.func, new_favorite)
