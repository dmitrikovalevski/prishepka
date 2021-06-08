from .models import Service
from .forms import ServiceForm
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView


class HomeTemplateView(TemplateView):
    template_name = 'base.html'


class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'service/all_services.html'


class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'service/service_id.html'


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





