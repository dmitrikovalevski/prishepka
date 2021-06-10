from .models import Service, Comments
from .forms import CommentsForm
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic.edit import FormMixin
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView,
                                  )


class HomeTemplateView(TemplateView):
    template_name = 'base.html'


class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'service/all_services.html'


# --- Сервис и комментарии к нему.
class ServiceDetailView(DetailView, FormMixin):
    model = Service
    context_object_name = 'service'
    template_name = 'service/service_id.html'
    form_class = CommentsForm




class ServiceCreateView(CreateView):
    model = Service
    fields = ['picture', 'title', 'descriptions', 'price']
    template_name = 'service/add_service.html'

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        service = form.save(commit=False)
        if self.request.user.is_authenticated:
            service.user = self.request.user
            service.save()
        return redirect(self.get_success_url())


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['picture', 'title', 'descriptions', 'price']
    template_name = 'service/update_service.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})


class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service/delete_service.html'
    success_url = 'home'

    def get_success_url(self):
        return reverse('home')


