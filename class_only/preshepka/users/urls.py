from django.urls import path

from .views import UserFormView, UserLogIn, UserLogOut

urlpatterns = [
    path('add/', UserFormView.as_view(), name='add_user'),
    path('login/', UserLogIn.as_view(), name='login'),
    path('logout/', UserLogOut.as_view(), name='logout'),
]