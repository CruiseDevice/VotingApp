from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('create_poll', views.create_poll, name='create_poll'),
    path('github_redirect', views.github_redirect, name='github_redirect'),
    path('twitter_redirect', views.twitter_redirect, name='twitter_redirect'),
    path('fcc_redirect', views.fcc_redirect, name='fcc_redirect'),
    path('my_polls', views.my_polls, name="my_polls"),
    path('share_twitter', views.share_twitter, name='share_twitter'),
    path('delete/<int:question_id>/', views.delete_poll, name='delete'),
]
