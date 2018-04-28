from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    url(
        r'^sign_in',
        views.sign_in,
        name='sign_in'
    ),
    url(
        r'sign_out',
        auth_views.logout ,
        name='sign_out'
    ),
    url(
        r'register',
        views.register,
        name='register'
    )
]