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
    )
]