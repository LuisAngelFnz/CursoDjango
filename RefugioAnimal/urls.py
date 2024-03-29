"""RefugioAnimal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView,
    logout_then_login,
    PasswordResetView,  PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)
from django.urls import path,include
# from apps.mascota.views import indexMascota

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/login/',  LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', logout_then_login, name='logout'),
    path('adopcion/', include('apps.adopcion.urls', namespace='adopcion')),
    path('mascota/',  include('apps.mascota.urls', namespace='mascota')),
    path('usuario/',  include('apps.usuario.urls', namespace='usuario')),
    path(
        'reset/password_reset',
        PasswordResetView.as_view(),
        {
            'template_name':'tpass_recovery/passwd_reset_form.html',
            'email_template_name':'tpass_recovery/passwd_reset_email.html'
        },
        name='password_reset'
    ),
    path(
        'reset/password_reset_done',
        PasswordResetDoneView.as_view(),
        {'template_name':'tpass_recovery/passwd_reset_done.html'},
        name='password_reset_done'
    ),
    path(
        'reset/password_reset_confirm/<slug:uidb64>/<slug:token>/',
        PasswordResetConfirmView.as_view(),
        {'template_name':'tpass_recovery/passwd_reset_confirm.html'},
        name='password_reset_confirm'
    ),
    path(
        'reset/password_reset_complete',
        PasswordResetCompleteView.as_view(),
        {'template_name':'tpass_recovery/passwd_reset_complete.html'},
        name='password_reset_complete'
    )
]
