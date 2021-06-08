from django.urls import reverse_lazy, reverse

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
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
