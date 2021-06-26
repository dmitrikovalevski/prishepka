from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, \
    PasswordResetDoneView, PasswordResetCompleteView

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView
from .forms import CreateUserForm, UserAccountUpdateForm, UpdateUserForm
from django.shortcuts import redirect, render


class UserFormView(CreateView):
    form_class = CreateUserForm
    template_name = 'users/add.html'

    def get_success_url(self):
        return reverse('login')


class UserLogIn(LoginView):
    pass


class UserLogOut(LogoutView):
    pass


class UserAccountView(DetailView):
    model = User
    template_name = 'users/account_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = self.request.user.pk == self.kwargs['pk']
        owner = User.objects.get(pk=self.kwargs['pk'])
        context['owner_services'] = owner.service_set.order_by('-date_created')
        return context


def update_user_account(request):
    # update user profile
    if request.method == 'POST':
        user_info = UserAccountUpdateForm(request.POST, request.FILES,
                                          instance=request.user.userinfo)
        user = UpdateUserForm(request.POST, instance=request.user)
        if user_info.is_valid() and user.is_valid():
            form = user_info.save()
            form.user = request.user
            form.save()
            user.save()
            return redirect('account', request.user.id)
    else:
        user_info = UserAccountUpdateForm(instance=request.user.userinfo)
        user = UpdateUserForm(instance=request.user)
    context = {
        'user_info': user_info,
        'user': user,
    }
    return render(request, 'users/account_update.html', context)


# reset password
class PasswordReset(PasswordResetView):
    template_name = 'registration/reset_form.html'


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'registration/reset_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'registration/reset_confirm.html'


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'registration/reset_complete.html'
