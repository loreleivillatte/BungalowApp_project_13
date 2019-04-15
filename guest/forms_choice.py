from django import forms
from .models import Post, List


class NewSentenceForm(forms.ModelForm):
    sentence = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Alexandrin', 'class': 'form-control'}), max_length=60)

    class Meta:
        model = Post
        fields = ['sentence']


class NewFavoriteForm(forms.ModelForm):
    author = forms.CharField(required=False)
    name = forms.CharField(required=False)

    class Meta:
        model = List
        fields = ['author', 'name']

    def clean_fields(self):
        author = self.cleaned_data.get('author').lower()
        name = self.cleaned_data.get('name').lower()
        return name, author

    def clean(self):
        author = self.cleaned_data.get('author')
        name = self.cleaned_data.get('name')
        if not author and not name:
            raise forms.ValidationError('Un champs requis')
        return self.cleaned_data
