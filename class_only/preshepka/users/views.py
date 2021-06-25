from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, \
    PasswordResetDoneView, PasswordResetCompleteView

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView
from .forms import CreateUserForm, UserAccountUpdateForm, UpdateUserForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group


class UserFormView(CreateView):
    form_class = CreateUserForm
    template_name = 'users/add.html'

    # # add user for group
    # def form_valid(self, form):
    #     user = form.save()
    #     if Group.objects.get(name='user'):
    #         user.groups.add(Group.objects.get(name='user').pk)
    #         user.save()
    #         return super().form_valid(form)
    #     else:
    #         group = Group.objects.create(name='user')
    #         user.groups.add(group)
    #         user.save()
    #         return super().form_valid(form)

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
    pass


class PasswordResetConfirm(PasswordResetConfirmView):
    pass


class PasswordResetDone(PasswordResetDoneView):
    pass


class PasswordResetComplete(PasswordResetCompleteView):
    pass
