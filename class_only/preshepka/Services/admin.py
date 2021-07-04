# Инструмент Django для работы с админкой
from django.contrib import admin

# Модели для админки
from .models import (
    Service,
    Comments,
)

# Добавим учлуги и комментарии в админку
admin.site.register(Service)
admin.site.register(Comments)
