# Направляет на шаблоны и указанные страницы
from django.shortcuts import render, redirect
# Модель
from .models import Service
# Форма модели для добавления и редактирования
from .froms import ServiceForm


def home(request):
    # Строим очередь из объектов
    service = Service.objects.order_by()
    # Добавляем очередь в контекст и выводим в шаблоне
    context = {
        'all_services': service
    }
    return render(request, 'service/index.html', context)


def view_service(request, pk):
    # Получаем услугу по ID
    get_service = Service.objects.get(pk=pk)
    # Добавляем очередь в контекст и выводим в шаблоне
    context = {
        'service': get_service
    }
    return render(request, 'service/view_service.html', context)


def add_service(request):
    # Получаем форму модели для заполнения
    new_service = ServiceForm()
    # Проверяем метод отправки из формы
    if request.method == 'POST':
        # Если метод ПОСТ то передадим полученые результаты в форму модели
        new_service = ServiceForm(request.POST)
        # Проверка на валидность\правильность заполнения
        if new_service.is_valid():
            # Если всё верно сохраняем форму
            new_service.save()
            # Переходим на указанную страницу
            return redirect('/')
    context = {
        'form': new_service
    }
    return render(request, 'service/add.html', context)


def edit_service(request, pk):
    # Получаем услугу по ID
    get_service = Service.objects.get(pk=pk)
    # Получаем форму модели для заполнения
    edit_form = ServiceForm()
    # Проверяем метод отправки из формы
    if request.method == 'POST':
        # Если метод ПОСТ тогда добавим в фому результат.
        # instance=get_service сравнивает полученную модель по ID с редактируемыми полями.
        # Это необходимо для редактирования модели.
        edit_form = ServiceForm(request.POST, instance=get_service)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('home')
    context = {
        'form': edit_form
    }
    return render(request, 'service/edit.html', context)


def delete_service(request, pk):
    get_service = Service.objects.get(pk=pk)
    get_service.delete()
    return redirect('home')
