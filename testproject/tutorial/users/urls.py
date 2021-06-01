from django.urls import path
from .views import user_account, create_user, login_user, logout_user
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('account/', user_account, name='account'),
    path('register/', create_user, name='registration'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

