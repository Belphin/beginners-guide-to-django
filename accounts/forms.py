from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class SignUpForm(UserCreationForm):
  email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
  role = forms.ChoiceField(choices=[('reader', 'Reader'), ('blogger', 'Blogger')])
  
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2', 'role')

  def save(self, commit=True):
    user = super().save(commit=False)
    if commit:
      user.save()
      role = self.cleaned_data.get('role')
      group, created  = Group.objects.get_or_create(name=role)
      user.groups.add(group)
    return user