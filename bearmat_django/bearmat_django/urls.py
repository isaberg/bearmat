"""bearmat_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include, url
from django.views import generic
from material.frontend import urls as frontend_urls
from bearmat import views as bearmat_views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('bearmat.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', bearmat_views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/veteran', bearmat_views.VeteranSignUpView.as_view(), name='veteran_signup'),
    path('accounts/signup/broker', bearmat_views.BrokerSignUpView.as_view(), name='broker_signup'),
]

# Defaults provided from django.contrib.auth.urls
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']
