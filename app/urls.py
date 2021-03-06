from django.conf.urls import url

from . import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^create_poll', views.create_poll, name='create_poll'),
    url(r'^github_redirect', views.github_redirect, name='github_redirect',),
    url(r'^twitter_redirect', views.twitter_redirect, name='twitter_redirect'),
    url(r'^fcc_redirect', views.fcc_redirect, name='fcc_redirect'),
    url(r'^my_polls', views.my_polls, name="my_polls"),
    url(r'^share_twitter', views.share_twitter, name='share_twitter'),
    url(r'^delete/(?P<question_id>[0-9]+)/', views.delete_poll, name='delete'),
]
