# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.utils.encoding import python_2_unicode_compatible
from django.shortcuts import render,get_list_or_404, \
                        get_object_or_404
from django.urls import reverse


from .models import Question, Choice

@python_2_unicode_compatible
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    print(latest_question_list)
    return render(request,'app/list.html',{'latest_question_list':latest_question_list})

@python_2_unicode_compatible
def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        print(question)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'app/detail.html',{
        'question':question
    })

@python_2_unicode_compatible
def vote(request, question_id):
    question = get_object_or_404(Question, id = question_id)
    try:
        selected_choice = question.choice_set.get(id = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'app/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('app:results', args=(question.id)))

@python_2_unicode_compatible
def results(request):
    return render(request, 'app/results.html',{})