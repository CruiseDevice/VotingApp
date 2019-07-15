from django import forms
from django.contrib.auth.models import User
from django.forms import formset_factory, modelformset_factory

from app.models import Question, Choice


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class QuestionModelForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question_text',)
        labels = {
            'question_text': 'Question'
        }
        widgets = {
            'question_text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your question here.'
            })
        }


QuestionModelFormset = modelformset_factory(
    Question,
    fields=('question_text',),
    extra=1,
    widgets={
        'question_text': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your question here'
        })
    }
)


ChoiceFormset = modelformset_factory(
    Choice,
    fields=('choice_text',),
    labels = {
        'choice_text': 'Choice',
    },
    extra=1,
    widgets={
        'choice_text': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your choices here.'
        })
    }
)