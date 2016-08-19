from django.db import (
	models
	)
from datetime import datetime
import time
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User)
	weight = models.IntegerField()
	height = models.IntegerField()
	MALE = 'Male'
	FEMALE = 'Female'
	GENDER_CHOICES = (
		(MALE,'Male'),
		(FEMALE, 'Female'),
		)
	gender = models.CharField(max_length = 6, choices = GENDER_CHOICES, default = MALE)
	def __str__(self):
		return self.user.username
class Weightgraph(models.Model):
	user = models.ForeignKey(User,related_name='weightgraph')
	weight = models.IntegerField()
	day = models.AutoField(primary_key = True)
	date = models.DateTimeField(default = datetime.now())
	def __str__(self):
		string = 'someday'
		return string
# workarounds for django chart-it
class ForGraphing(models.Model):
	user = models.OneToOneField(User)
	bmi = models.FloatField()
	ibw = models.FloatField()
	ibw_hamwi = models.FloatField()
	current_weight = models.IntegerField(default=190)
	def __str__(self):
		string = 'data'
		return string
#for level progressions graph
# saves on every entry to user dashboard (so every login or every navigation to the user dashboard)
class LevelsGraph(models.Model):
	user = models.ForeignKey(User, related_name="levelsgraph")
	abslevel = models.FloatField()
	leg = models.FloatField()
	upperarm = models.FloatField()
	lowerarm = models.FloatField()
	back = models.FloatField()
	chest = models.FloatField()
	glutes = models.FloatField()
	neck = models.FloatField()
	overall = models.FloatField()
	date = models.DateTimeField(default = datetime.now())
	def __str__(self):
		string = 'levels'
		return string
'''
#<<< Updating model when i want to only UPDATE the values in this field
#c = Calculations.objects.get(user=request.user)
#c.weight_for_calc = 999  # change weight field(s) in pounds as needed
#c.height_for_calc = 998  # change height field(s) in inches as needed
#c.save() >>>
#Biggest model
'''
class Calculations(models.Model):
	user = models.OneToOneField(User)
	height_for_calc = models.IntegerField()
	weight_for_calc = models.IntegerField()
	bmi = models.IntegerField()
	gender = models.CharField(max_length=6, default="Male")
	def _get_bmi(self):
		calc_bmi = (self.weight_for_calc * 0.45) / ((self.height_for_calc * 0.025)**2)
		return calc_bmi
	bmi = property(_get_bmi)
	def _get_ibw_devine(self):
		if self.gender == 'Male':
			ibw = 110 + 5.1 * (self.height_for_calc - 60)
		if self.gender == 'Female':
			ibw = 100 + 5.1 * (self.height_for_calc - 60)
		return ibw
	user_ibw = property(_get_ibw_devine)
	def _get_ibw_hamwi(self):
		if self.gender == 'Male':
			ibw_h = 106 + 6 * (self.height_for_calc - 60)
		if self.gender == 'Female':
			ibw_h = 100 + 5 * (self.height_for_calc - 60)
		return ibw_h 
	user_ibw_hamwi = property(_get_ibw_hamwi)
	#max rep test
	lunges = models.IntegerField()
	sit_ups = models.IntegerField()
	push_ups = models.IntegerField()
	squats = models.IntegerField()
	calf_raises = models.IntegerField()
	#levels - redo abs, back, and neck
	def get_abs_level(self):
		level_abs = 20
		return level_abs
	abs_level = property(get_abs_level)
	def get_leg_level(self):
		actual_weight = self.weight_for_calc
		adjusted_weight = self.weight_for_calc * 0.72
		max_reps = self.squats
		one_rm = adjusted_weight * (max_reps**0.1)
		if one_rm < actual_weight:
			level_leg = one_rm/actual_weight * 50
		else:
			level_leg = (one_rm/actual_weight * 100) + 50
		return level_leg
	leg_level = property(get_leg_level)
	def get_uarm(self):
		actual_weight = self.weight_for_calc
		adjusted_weight = self.weight_for_calc * 0.72
		max_reps = self.push_ups
		one_rm = adjusted_weight * (max_reps**0.1)
		if one_rm < actual_weight:
			level_uarm = one_rm/actual_weight * 50
		if one_rm > actual_weight:
			level_uarm = (one_rm/actual_weight * 100) + 50
		return level_uarm
	uarm_level = property(get_uarm)
	def get_larm(self):
		actual_weight = self.weight_for_calc
		adjusted_weight = self.weight_for_calc * 0.72
		max_reps = self.push_ups
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
		actual_weight = self.weight_for_calc
		adjusted_weight = self.weight_for_calc * 0.72
		max_reps = self.push_ups
		one_rm = adjusted_weight * (max_reps**0.1)
		if one_rm < actual_weight:
			level_chest = one_rm/actual_weight * 50
		if one_rm > actual_weight:
			level_chest = (one_rm/actual_weight * 100) + 50
		return level_chest
	cht_level = property(get_chest)
	def get_glutes(self):
		actual_weight = self.weight_for_calc
		adjusted_weight = self.weight_for_calc * 0.72
		max_reps = self.squats
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
	def __str__(self):
		rndm_name = 'calculation'
		return rndm_name
#Exercise database implementation
class Exercise(models.Model):
	ex_key = models.CharField(max_length=5)
	ex_name = models.CharField(max_length=250)
	ex_type = models.CharField(max_length=30)
	ex_dif = models.CharField(max_length=30)
	image_name = models.CharField(max_length=100)
	directions = models.CharField(max_length=10000)
	categories = models.CharField(max_length=200)
	def __str__(self):
		return self.ex_name
	def grab_exercise(self):
		array = [self.ex_key,self.ex_name,self.ex_type,self.ex_dif]
		return array
'''
# Secret Calculator model
class SecretCalculator(models.Model):
	user = models.OneToOneField(User)
	abslevel = models.FloatField()
	leg = models.FloatField()
	upperarm = models.FloatField()
	lowerarm = models.FloatField()
	back = models.FloatField()
	chest = models.FloatField()
	glutes = models.FloatField()
	neck = models.FloatField()
	abs_ex = models.FloatField()
	leg_ex = models.FloatField()
	uarm_ex = models.FloatField()
	larm_ex = models.FloatField()
	back_ex = models.FloatField()
	cht_ex = models.FloatField()
	glu_ex = models.FloatField()
	nec_ex = models.FloatField()
	def absex(self):
		new = self.abslevel + self.abs_ex
		return new
	new_abs = property(absex)
	def legex(self):
		new = self.leg + self.leg_ex
		return new 
	new_leg = property(legex)
	def uarmex(self):
		new = self.upperarm + self.uarm_ex
		return new 
	new_uarm = property(uarmex)
	def larmex(self):
		new = self.lowerarm + self.larm_ex
		return new
	new_larm = property(larmex)
	def backex(self):
		new = self.back + self.back_ex
		return new
	new_back = property(backex)
	def chtex(self):
		new = self.chest + self.cht_ex
		return new
	cht_ex = property(chtex)
	def gluex(self):
		new = self.glutes + self._ex
		return new
	glu_ex = property(gluex)
	def necex(self):
		the_experience = 0
		string = self.exercise.categories
		if 'Chest' in string:
			if self.weight == 0:
				the_experience = self.sets * self.reps * 0.5
			else:
				the_experience = self.sets * self.reps * 0.3275
		return the_experience
	nec_ex = property(necex)
'''

#<<< Using exercise key to add
#add exercise from web as long as i have exercise key i can declare Exercise object
# ex = Exercise(ex_key = exercise_key) then use as such
#ExerciseRoutine(user=request.user, exercise = ex)
# then have a form which adds in the remaining fields 
#>>>
class ExerciseRoutine(models.Model):
	user = models.ForeignKey(User , related_name = 'routine')
	exercise = models.ForeignKey('Exercise', on_delete = models.CASCADE)
	sets = models.IntegerField()
	reps = models.IntegerField()
	weight = models.IntegerField(default=0)
	DAYONE = 'DayOne'
	DAYTWO = 'DayTwo'
	DAYTHREE = 'DayThree'
	DAY_CHOICES = (
		(DAYONE,'DayOne'),
		(DAYTWO,'DayTwo'),
		(DAYTHREE,'DayThree'),
		)
	day = models.CharField(max_length = 8, choices = DAY_CHOICES, default = DAYONE)
	def absex(self):
		the_experience = 0
		string = self.exercise.categories
		if 'Abs' in string:
			the_experience = self.sets * self.reps * 0.5
			return the_experience
	abs_ex = property(absex)
	def legex(self):
		the_experience = 0
		string = self.exercise.categories
		if 'Abductors' or 'Adductors' or 'Calves' or 'Hamstrings' in string:
			if self.weight == 0:
				the_experience = self.sets * self.reps * 0.5
			else:
				the_experience = self.sets * self.reps * 0.3275
		return the_experience 
	leg_ex = property(legex)
	def uarmex(self):
		the_experience = 0
		string = self.exercise.categories
		if 'Biceps' or 'Triceps' in string:
			if self.weight == 0:
				the_experience = self.sets * self.reps * 0.5
			else:
				the_experience = self.sets * self.reps * 0.3275
		return the_experience 
	uarm_ex = property(uarmex)
	def larmex(self):
		the_experience = 0
		string = self.exercise.categories
		if 'Forearms' in string:
			if self.weight == 0:
				the_experience = self.sets * self.reps * 0.5
			else:
				the_experience = self.sets * self.reps * 0.3275
		return the_experience
	larm_ex = property(larmex)
	def backex(self):
		the_experience = 0
		string = self.exercise.categories
		if 'Lats' or 'Lower' or 'Middle' or 'Traps' in string:
			if self.weight == 0:
				the_experience = self.sets * self.reps * 0.5
			else:
				the_experience = self.sets * self.reps * 0.3275
		return the_experience
	back_ex = property(backex)
	def chtex(self):
		the_experience = 0
		string = self.exercise.categories
		if 'Chest' in string:
			if self.weight == 0:
				the_experience = self.sets * self.reps * 0.5
			else:
				the_experience = self.sets * self.reps * 0.3275
		return the_experience
	cht_ex = property(chtex)
	def gluex(self):
		the_experience = 0
		string = self.exercise.categories
		if 'Glutes' in string:
			if self.weight == 0:
				the_experience = self.sets * self.reps * 0.5
			else:
				the_experience = self.sets * self.reps * 0.3275
		return the_experience
	glu_ex = property(gluex)
	def necex(self):
		the_experience = 0
		string = self.exercise.categories
		if 'Chest' in string:
			if self.weight == 0:
				the_experience = self.sets * self.reps * 0.5
			else:
				the_experience = self.sets * self.reps * 0.3275
		return the_experience
	nec_ex = property(necex)
	def __str__(self):
		string = "routine"
		return string
	#def delete(self):
	#	x = SecretCalculator.objects.filter(user=self.user).update(abs_ex += self.abs_ex, leg_ex += self.leg_ex, uarm_ex += self.uarm_ex, larm_ex += self.larm_ex, back_ex += self.back_ex, cht_ex += self.cht_ex, glu_ex += self.glu_ex, nec_ex += self.nec_ex)
	#	x.save()
	#	super(ExerciseRoutine, self).delete()
