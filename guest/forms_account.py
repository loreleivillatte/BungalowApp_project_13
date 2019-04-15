from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Speudo', 'class': 'form-control'}
    ))
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control'}
    ))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Mot de passe', 'class': 'form-control'}
    ))
    confirm_password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirmer mot de passe', 'class': 'form-control'}
    ))


class AuthForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Speudo', 'class': 'form-control'}
    ))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Mot de passe', 'class': 'form-control'}
    ))
