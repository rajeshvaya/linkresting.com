from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SignupForm(UserCreationForm):
	name = forms.CharField(required=True)
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("name", 'email', 'password1', 'password2')
		exclude = ("username",)

class PasswordResetFormExtend(PasswordResetForm):
	def __init__(self, *args, **kwargs):
		super(PasswordResetFormExtend, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Reset', css_class='btn btn-danger'))

