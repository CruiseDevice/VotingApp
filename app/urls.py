from django.conf.urls import url

from . import views

app_name = 'app'

urlpatterns = [
    # ex: /app/
    url(
        r'^$',
        views.index,
        name='index'
    ),
    url(
        r'^(?P<question_id>[0-9]+)/$',
        views.detail,
        name='detail'
    ),
    url(
        r'^(?P<question_id>[0-9]+)/vote/$',
        views.vote,
        name='vote'
    ),
    url(
        r'^(?P<question_id>[0-9]+)/results/$',
        views.results,
        name='results'
    ),
    url(
        r'^new/$',
        views.new_poll,
        name='new_poll'
    ),
    url(
        r'^new/addNewQuestion',
        views.addNewQuestion,
        name='addNewQuestion'
    ),
    url(
        r'^new/addNewChoice',
        views.addNewChoice,
        name='addNewChoice',
    ),
    url(
        r'^github_redirect',
        views.github_redirect,
        name='github_redirect',
    ),
    url(
        r'twitter_redirect',
        views.twitter_redirect,
        name='twitter_redirect'
    ),
    url(
        r'fcc_redirect',
        views.fcc_redirect,
        name='fcc_redirect'
    )
]