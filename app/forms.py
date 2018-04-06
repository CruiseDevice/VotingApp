from django import forms
from django.contrib.auth.models import User
from app.models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('question','choice_text',)

