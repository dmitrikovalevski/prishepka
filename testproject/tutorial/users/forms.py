# Готовая django для создания пользователя
from django.contrib.auth.forms import UserCreationForm
# Готовая модель пользователя на которой построится форма
from django.contrib.auth.models import User

# Класс формы
class NewUserForm(UserCreationForm):
    class Meta:
        # Модель пользователя
        model = User
        # Поля из модели которые будут использованы при регистрации
        fields = ['username', 'email', 'password1', 'password2']

