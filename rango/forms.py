from django import forms
from django.contrib.auth.models import User
from .models import (
	Weightgraph,
	Profile,
	Calculations,
	ExerciseRoutine
	)
class WeightForm(forms.ModelForm):
	weight = forms.IntegerField(help_text="Enter Weight")
	class Meta:
		model = Weightgraph
		fields = ('weight',)
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username','email','password')
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('weight','height','gender')
class CalcForm(forms.ModelForm):
	lunges = forms.IntegerField(help_text="Enter Maximum Reps of lunges")
	sit_ups = forms.IntegerField(help_text="Enter Maximum Reps of sit-ups")
	push_ups = forms.IntegerField(help_text="Enter Maximum Reps of push-ups")
	squats = forms.IntegerField(help_text="Enter Maximum Reps of squats")
	calf_raises = forms.IntegerField(help_text="Enter Maximum Reps of calf raises")
	class Meta:
		model = Calculations
		fields = ('lunges','sit_ups','push_ups','squats','calf_raises')
class RoutineForm(forms.ModelForm):
	class Meta:
		model = ExerciseRoutine
		fields = ('sets','reps','weight','day')