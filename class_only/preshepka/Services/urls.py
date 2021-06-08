from django.urls import path
from .views import ServiceListView, ServiceDetailView, ServiceCreateView

urlpatterns = [
    path('', ServiceListView.as_view(), name='home'),
    path('detail/<int:pk>', ServiceDetailView.as_view(), name='detail'),
    path('add_service/', ServiceCreateView.as_view(), name='add_service'),
]