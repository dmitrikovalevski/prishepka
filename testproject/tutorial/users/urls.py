from django.urls import path
from .views import user_account, create_user, login_user, logout_user

urlpatterns = [
    path('account/', user_account, name='account'),
    path('register/', create_user, name='registration'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]