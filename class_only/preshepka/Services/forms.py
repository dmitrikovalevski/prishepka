# Модели
from .models import Comments

# Инструмент Django для создания форм
from django import forms


# Форма для комментария

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
