# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.http import (
     Http404, HttpResponseRedirect, HttpResponse
)
from django.utils.encoding import python_2_unicode_compatible
from django.shortcuts import (
    render,get_list_or_404,get_object_or_404, redirect
)
from django.forms import (
    modelformset_factory,
)
from django.db import transaction
from django.urls import reverse
from django.utils import  timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from .forms import (
    ChoiceForm, QuestionForm,
    UserRegistrationForm, ChoiceFormSet
)

from .models import Question, Choice

@python_2_unicode_compatible
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')
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

# @login_required
# @python_2_unicode_compatible
# def addNewQuestion(request):
#     questionForm = QuestionForm(request.POST or None)
#     choiceFormSet = modelformset_factory(Choice, form=ChoiceForm, extra=4)
#     # queryset = Question.objects.get()
#     formset = choiceFormSet(request.POST or None, queryset=None)
#     if questionForm.is_valid() and formset.is_valid():
#         instances = formset.save(commit=False)
#         for instance in instances:
            
#             instance.save()
#     return render(request, 'app/newQuestion.html',{
#         'questionForm':questionForm,
#         'formset':formset,
#     })
    # https://stackoverflow.com/questions/9743103/django-how-to-limit-field-choices-in-formset
    # formset for choices django
    # https://stackoverflow.com/questions/9012033/django-modelform-has-no-model-class-specified
    # https://stackoverflow.com/questions/25602279/formset-object-object-has-no-attribute-fields
    # https://whoisnicoleharris.com/2015/01/06/implementing-django-formsets.html
    # ChoiceFormSet = formset_factory(ChoiceForm, formset=BaseFormSet)

    
class AddNewQuestion(CreateView):
    model = Question
    template_name = 'app/newQuestion.html'
    fields = ['question_text']
    success_url = reverse_lazy('app:index')

    def get_context_data(self, **kwargs):
        data = super(AddNewQuestion, self).get_context_data(**kwargs)
        if self.request.POST:
            data['choiceset'] = ChoiceFormSet(self.request.POST)
        else:
            data['choiceset'] = ChoiceFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        choiceset = context['choiceset']
        with transaction.atomic():
            self.object = form.save()

            if choiceset.is_valid():
                choiceset.instance = self.object
                choice.save()
        return super(AddNewQuestion, self).form_valid(form)



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

def my_polls(request):
    user = None
    logged_in_user = request.user
    logged_in_user_polls = Question.objects.filter(user=user)
    return render(request,'app/my_polls.html',{
        'polls':logged_in_user_polls
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
            return render(request,'registration/register_done.html',{
                'new_user':new_user
            })
    else:
        user_form = UserRegistrationForm()

    return render(request, 'registration/register.html',{
        'user_form':user_form
    })
