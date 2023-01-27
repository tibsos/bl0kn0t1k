from django.urls import path

from django.contrib.auth.views import LogoutView
from .views import *
from .password_recovery_views import *

from django.conf import settings

app_name = 'user'

urlpatterns = [

    path('login/', log_in, name = 'login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name = 'logout'),
    path('register/', register, name = 'register'),

    path('confirm_email/', ce, name = 'ce'),

    path('forgot-password/', forgot_password, name = 'forgot-password'),
    path('recover/', send_recovery_email, name = 'recover'),
    path('reset-password/<uuid:password_recovery_token>/', reset_password, name = 'reset-password'),

    path('toggle-mode/', toggle_mode, name = 'toggle-mode'),

]