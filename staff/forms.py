from django import forms
from guest.models import Message, Topic


class NewMessageForm(forms.ModelForm):

    content = forms.CharField(required=True,  widget=forms.Textarea(attrs={
        'placeholder': 'message', 'class': 'form-control'}), max_length=4000)

    class Meta:
        model = Message
        fields = ['content']


class NewTopicForm(forms.ModelForm):
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'question', 'class': 'form-control'}), max_length=200)

    reply_1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'choix n°1', 'class': 'form-control'}), max_length=30)

    reply_2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'choix n°2', 'class': 'form-control'}), max_length=30)

    class Meta:
        model = Topic
        fields = ['subject', 'reply_1', 'reply_2']
