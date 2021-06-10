from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView, ListView
from .forms import CreateUserForm


class UserFormView(CreateView):
    form_class = CreateUserForm
    template_name = 'users/add.html'

    def get_success_url(self):
        return reverse('home')


class UserLogIn(LoginView):
    pass


class UserLogOut(LogoutView):
    pass


class UserAccountListView(ListView):
    model = User
    template_name = 'users/account.html'
