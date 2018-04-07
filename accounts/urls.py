from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [
    url(
        r'^signin',
        views.sign_in,
        name='sign_in'
    )
]