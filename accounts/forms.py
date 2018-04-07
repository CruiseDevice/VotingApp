from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

class AccountForm(forms.Form):
    def addError(self,message):
        self._errors[NON_FIELD_ERRORS] = self.error_class([message])

class SigninForm(AccountForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(render_value=False)
    )

# class RegisterForm(AccountForm):
#     name = forms.CharField()