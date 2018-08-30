from django import forms
from django.contrib.auth.models import User
from app.models import Question, Choice
from django.forms.widgets import RadioSelect
from django.forms import inlineformset_factory

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        # fields = ('question_text',)
        exclude = ()

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        # fields = ('choice_text',)
        exclude = ()

ChoiceFormSet = inlineformset_factory(Question, Choice, form=ChoiceForm, 
                    extra=4)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('username','first_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']