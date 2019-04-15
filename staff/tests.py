from django.urls import reverse
from django.test import TestCase
from staff.forms import NewTopicForm, NewMessageForm


class IndexTests(TestCase):
    def test_index_view_status_code(self):
        url = reverse('index_staff')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)


    def test_dash_view_status_code(self):
        url = reverse('dash')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_user_view_status_code(self):
        url = reverse('users')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_list_view_status_code(self):
        url = reverse('list', args=['1'])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_new_topic_view_status_code(self):
        url = reverse('new_topic')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_topic_view_status_code(self):
        url = reverse('topics')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_detail_topic_view_status_code(self):
        url = reverse('detail_topic', args=['1'])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_random_user_view_status_code(self):
        url = reverse('random_message')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_sent_user_view_status_code(self):
        url = reverse('sent_user', args=['1'])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_logout_view_status_code(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)


class TestForms(TestCase):

    def test_new_topic_form_valid_data(self):
        form_data = {
            'subject': 'subject',
            'reply_1': 'a',
            'reply_2': 'b',
        }
        form = NewTopicForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid_data(self):
        form_data = {}
        form = NewTopicForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_auth_form_valid_data(self):
        form_data = {
            'content': 'content',
        }
        form = NewMessageForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_auth_form_invalid_data(self):
        form_data = {}
        form = NewMessageForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
