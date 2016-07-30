from __future__ import unicode_literals

from django.db import models
import csv
import math
# Create your models here.
from django.db import models
#just in case
import csv
#to access User
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.
#model exercise
# grab_exercise() function which will allow us to access the components of ex class
class Exercise(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
	def grab_exercise(self):
		array = [self.ex_key,self.ex_name,self.ex_type,self.ex_dif]
		return array
#Muscle Group Databases
class Abs(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class Shoulders(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class Glutes(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class Hamstrings(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class Lower_Back(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class Lats(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class Quadriceps(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class Triceps(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class Calves(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class Forearms(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class Traps(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class Abductors(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class Adductors(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class Middle_Back(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class Biceps(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class Chest(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class Neck(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	def __str__(self):
		return self.ex_name
class UsersProfile(models.Model):
	user = models.OneToOneField(User) #link to user
	height = models.IntegerField(null = True)
	weight = models.IntegerField(null = True)
	gender = models.CharField(max_length=6)
	def get_weight(self):
		return self.weight
	def _get_bmi(self):
		bmi = (self.weight * 0.45) / ((self.height * 0.025)**2)
		return bmi
	user_bmi = property(_get_bmi)
	def _get_ibw_devine(self):
		if self.gender == 'Male':
			ibw = 110 + (5.1 * self.height) - 60
		if self.gender == 'Female':
			ibw = 100 + (5.1 * self.height) - 60
		return ibw
	user_ibw = property(_get_ibw_devine)
	def _get_ibw_hamwi(self):
		if self.gender == 'Male':
			ibw_h = 106 + (6 * self.height) - 60
		if self.gender == 'Female':
			ibw_h = 100 + (5 * self.height) - 60
		return ibw_h 
	user_ibw_hamwi = property(_get_ibw_hamwi)
	def __str__(self):
		return self.user.username
	maxreplunges = models.IntegerField(null = True)
	maxrepsitups = models.IntegerField(null = True)
	maxreppushups = models.IntegerField(null = True)
	maxrepsquats = models.IntegerField(null = True)
	maxrepcalfraises = models.IntegerField(null = True)
	def get_abs_level(self):
		level_abs = 20
		return level_abs
	abs_level = property(get_abs_level)
	def get_leg_level(self):
		actual_weight = self.weight
		adjusted_weight = self.weight * 0.72
		max_reps = self.maxrepsquats
		one_rm = adjusted_weight * (max_reps**0.1)
		if one_rm < actual_weight:
			level_leg = one_rm/actual_weight * 50
		else:
			level_leg = (one_rm/actual_weight * 100) + 50
		return level_leg
	leg_level = property(get_leg_level)
	def get_uarm(self):
		actual_weight = self.weight
		adjusted_weight = self.weight * 0.72
		max_reps = self.maxreppushups
		one_rm = adjusted_weight * (max_reps**0.1)
		if one_rm < actual_weight:
			level_uarm = one_rm/actual_weight * 50
		if one_rm > actual_weight:
			level_uarm = (one_rm/actual_weight * 100) + 50
		return level_uarm
	uarm_level = property(get_uarm)
	def get_larm(self):
		actual_weight = self.weight
		adjusted_weight = self.weight * 0.72
		max_reps = self.maxreppushups
		one_rm = adjusted_weight * (max_reps**0.1)
		if one_rm < actual_weight:
			level_larm = (one_rm/actual_weight * 50) / 2
		if one_rm > actual_weight:
			level_larm = (one_rm/actual_weight * 100) + 50
		return level_larm
	larm_level = property(get_larm)
	def get_back(self):
		level_back = 45
		return level_back
	back_level = property(get_back)
	def get_chest(self):
		actual_weight = self.weight
		adjusted_weight = self.weight * 0.72
		max_reps = self.maxreppushups
		one_rm = adjusted_weight * (max_reps**0.1)
		if one_rm < actual_weight:
			level_chest = one_rm/actual_weight * 50
		if one_rm > actual_weight:
			level_chest = (one_rm/actual_weight * 100) + 50
		return level_chest
	cht_level = property(get_chest)
	def get_glutes(self):
		actual_weight = self.weight
		adjusted_weight = self.weight * 0.72
		max_reps = self.maxreppushups
		one_rm = adjusted_weight * (max_reps**0.1)
		if one_rm < actual_weight:
			level_glutes = one_rm/actual_weight * 50
		if one_rm > actual_weight:
			level_glutes = (one_rm/actual_weight * 100) + 50
		return level_glutes
	glu_level = property(get_glutes)
	def get_neck(self):
		neck_level = 20
		return neck_level
	nec_level = property(get_neck)
	def get_overall(self):
		overall_sum = self.abs_level + self.leg_level + self.uarm_level + self.larm_level + self.back_level + self.cht_level + self.glu_level
		overall_level = overall_sum / 7
		return overall_level
	overall = property(get_overall)