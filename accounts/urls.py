from django.urls import path, re_path
from accounts import views
from django.contrib.auth.views import (login, logout,
                                       password_reset,
                                       password_reset_done,
                                       password_reset_confirm,
                                       password_reset_complete
                                       )

app_name = "accounts"
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login, {'template_name': 'accounts/login.html',
                           'redirect_field_name': '/accounts/register/'}, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('reset-password/', password_reset, {'template_name': 'accounts/reset_password.html',
                                             'post_reset_redirect': 'accounts:password_reset_done',
                                             'email_template_name': 'accounts/reset_password_email.html'},
         name='reset_password'),
    path('reset-password-done/', password_reset_done, {"template_name": 'accounts/reset_password_done.html'},
         name='password_reset_done'),
    path('reset-password/confirm/?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/',
         password_reset_confirm, {"template_name": 'accounts/reset_password_confirm.html',
                                  'post_reset_redirect': 'accounts:password_reset_complete'},
         name='password_reset_confirm'),
    path('reset-password/complete/', password_reset_complete,
         {"template_name": 'accounts/reset_password_complete.html'},
         name='password_reset_complete'),
]
