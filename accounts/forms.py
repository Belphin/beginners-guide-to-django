from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class SignUpForm(UserCreationForm):
	email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

	READER = 0
	BLOGGER = 1

	ROLE_TYPE = (
		(READER, "Reader"),
		(BLOGGER, "Blogger"),
	)

	role = forms.ChoiceField(choices=ROLE_TYPE)
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'role')