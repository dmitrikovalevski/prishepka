from django.urls import path
from .views import (ServiceListView, ServiceDetailView,
                    ServiceCreateView, ServiceUpdateView,
                    ServiceDeleteView)

urlpatterns = [
    path('', ServiceListView.as_view(), name='home'),
    path('detail/<int:pk>/', ServiceDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', ServiceUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ServiceDeleteView.as_view(), name='delete'),
    path('add_service/', ServiceCreateView.as_view(), name='add_service'),
]