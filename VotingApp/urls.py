"""VotingApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import(
    login, logout, logout_then_login,
    password_reset, password_reset_done,
    password_reset_confirm, password_reset_complete,
    password_change, password_change_done
) 

from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('app.urls')),
    url(
       r'^oauth/',
       include('social_django.urls',namespace='social')
    )
]

urlpatterns += [
    url(r'^accounts/login/$',login,name='login'),
    url(r'^accounts/register/$',views.register,name='register'),
    url(r'^accounts/logout/$',logout,name='logout'),
    url(r'^accounts/logout-then-login/$',
            logout_then_login,name='logout_then_login'),
    url(r'^accounts/password-change/$', 
            password_change,name='password_change'),
    url(r'^accounts/password-change/done/$', 
            password_change_done,name='password_change_done'),
    url(r'^accounts/password-reset/$',
            password_reset,name='password_reset'),
    url(r'^accounts/password-reset/done/$',
            password_reset_done,name='password_reset_done'),
    url(r'^accounts/password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
            password_reset_confirm,name='password_reset_confirm'),
    url(r'^accounts/password-reset/complete/$',
            password_reset_complete,name='password_reset_complete'),

]