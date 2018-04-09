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

class RegisterForm(AccountForm):
    name = forms.CharField(required = True)
    email = forms.EmailField(required=True)
    password = forms.CharField(
        required=True,
        label=(u'Password'),
        widget=forms.PasswordInput(
            render_value=False
        )
    )
    ver_password=forms.CharField(
        required=True,
        label = (u'Verify Password'),
        widget = forms.PasswordInput(
            render_value=False
        )
    )

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')
        ver_password = cleaned_data.get('ver_password')
        if password != ver_password:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data