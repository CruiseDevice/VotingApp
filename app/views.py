# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.utils.encoding import python_2_unicode_compatible
from django.shortcuts import render,get_list_or_404, \
                        get_object_or_404, redirect
from django.urls import reverse
from django.utils import  timezone

from .forms import ChoiceForm, QuestionForm

from .models import Question, Choice

@python_2_unicode_compatible
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # print(latest_question_list)
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
        selected_choice.votes = selected_choice.votes + 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('app:results', args=(question.id,)))

@python_2_unicode_compatible
def results(request,question_id):
    question = get_object_or_404(Question, id = question_id)
    colors = ['Yellow','Brown','Red','Green','Blue']
    return render(request, 'app/results.html',{
        'question':question,
        'colors':colors
    })

@python_2_unicode_compatible
def new_poll(request):
    return render(request,'app/new_poll.html',{})

@python_2_unicode_compatible
def addNewQuestion(request):
    print("addnewquestion")
    if request.method == "POST":
        print("inside if inside addnewquestion")
        form = QuestionForm(request.POST)
        print(form)
        if form.is_valid():
            print(form.is_valid())
            post = form.save()
            post.pub_date = timezone.now()
            post.save()
            print(post)
            return redirect('app:new_poll')
    else:
        form=QuestionForm()
    return render(request,'app/newQuestion.html',{
        'form':form
    })

@python_2_unicode_compatible
def addNewChoice(request):
    if request.method == "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('app:new_poll')
    else:
        form = ChoiceForm()
    return render(request,'app/newChoice.html',{
        'form':form
    })

def github_redirect(request):
    return redirect("https://github.com/CruiseDevice")

def twitter_redirect(request):
    return redirect("https://twitter.com/CruiseDevice")

def fcc_redirect(request):
    return redirect("https://www.freecodecamp.org/challenges/build-a-voting-app")

def my_polls(request,user):
    logged_in_user = request.user
    logged_in_user_polls = Question.objects.filter(user=user)
    return render(request,'my_polls.html',{
        'polls':logged_in_user_polls
    })