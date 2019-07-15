# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.http import (
     Http404, HttpResponseRedirect, HttpResponse
)
from django.utils.encoding import python_2_unicode_compatible
from django.shortcuts import (
    render, get_list_or_404, get_object_or_404, redirect
)
from django.forms import (
    modelformset_factory,
)
from django.db import transaction
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import (
    UserRegistrationForm,
    QuestionModelForm, ChoiceFormset
)

from .models import Question, Choice


@python_2_unicode_compatible
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')

    return render(request, 'app/question_list.html', {
        'latest_question_list': latest_question_list
    })


@login_required
@python_2_unicode_compatible
def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'app/detail.html', {
        'question': question
    })


@login_required
@python_2_unicode_compatible
def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(
            id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'app/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes = selected_choice.votes + 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('app:results', args=(question.id,)))


@login_required
@python_2_unicode_compatible
def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    colors = ['Yellow', 'Brown', 'Red', 'Green', 'Blue']
    return render(request, 'app/results.html', {
        'question': question,
        'colors': colors
    })


def github_redirect(request):
    return redirect("https://github.com/CruiseDevice")


def twitter_redirect(request):
    return redirect("https://twitter.com/CruiseDevice")


def fcc_redirect(request):
    return redirect(
            "https://www.freecodecamp.org/challenges/build-a-voting-app")


def share_twitter(request):
    return redirect("https://twitter.com")


@login_required
def my_polls(request):
    user = None
    logged_in_user = request.user
    logged_in_user_polls = Question.objects.filter(user=logged_in_user)
    return render(request, 'app/my_polls.html', {
        'polls': logged_in_user_polls
    })


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            return render(request, 'registration/register_done.html', {
                'new_user': new_user
            })
    else:
        user_form = UserRegistrationForm()

    return render(request, 'registration/register.html', {
        'user_form': user_form
        })


def create_poll(request):
    user = request.user
    if request.method == "GET":
        questionform = QuestionModelForm(request.GET or None)
        formset = ChoiceFormset(queryset=Choice.objects.none())
    elif request.method == "POST":
        questionform = QuestionModelForm(request.POST)
        formset = ChoiceFormset(request.POST)
        if questionform.is_valid() and formset.is_valid():
            question = questionform.save(commit=False)
            question.user = user
            question.save()
            for form in formset:
                choice = form.save(commit=False)
                choice.question = question
                choice.save()
            return redirect('app:index')
    return render(request, 'app/create_poll.html', {
            'questionform': questionform,
            'formset': formset
    })


def delete_poll(request, question_id):
    if question_id:
        question = get_object_or_404(Question, id=question_id)
        if question:
            question.choice_set.all().delete()
            question.delete()
    return redirect('app:index')