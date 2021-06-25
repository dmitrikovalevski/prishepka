from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserInfo


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class UserAccountUpdateForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['image', 'phone']
