from .models import Service, Comments, Rubric

from django import forms


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['picture', 'title', 'descriptions', 'price', 'user']


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']


class RubricForm(forms.ModelForm):
    class Meta:
        model = Rubric
        fields = ['name']
