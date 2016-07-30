# adding in libraries for user
from django import forms
from django.contrib.auth.models import User
from .models import UsersProfile 

#Form for basic user creation
class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UsersProfile
		fields = {'height','weight','gender','maxreplunges','maxrepsitups','maxreppushups','maxrepsquats','maxrepcalfraises'}