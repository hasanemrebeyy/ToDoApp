from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class UserForm(forms.Form):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name'})
        self.fields['email'].widget = TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'E-mail'})
        self.fields['password'].widget = TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'})
