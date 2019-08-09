from django.db import (
	models
	)
from datetime import datetime
import time
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.validators import (
	MaxValueValidator,
	MinValueValidator
	)
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
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
	user = models.ForeignKey(User,related_name='weightgraph',on_delete=models.CASCADE)
	weight = models.IntegerField()
	day = models.AutoField(primary_key = True)
	date = models.DateTimeField(default = datetime.now())
	def __str__(self):
		string = 'someday'
		return string
# workarounds for django chart-it
class ForGraphing(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	bmi = models.FloatField()
	ibw = models.FloatField()
	ibw_hamwi = models.FloatField()
	current_weight = models.IntegerField(default=190)
	def __str__(self):
		string = 'data'
		return string
#for level progressions graph
# saves on every entry to user dashboard (so every login or every navigation to the user dashboard)
class LevelGrowthGraph(models.Model):
	user = models.ForeignKey(User, related_name="levelsgraph",on_delete=models.CASCADE)
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
	month = models.IntegerField(default = datetime.now().month)
	year = models.IntegerField(default = datetime.now().year)
	day = models.IntegerField(default = datetime.now().day)
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
	user = models.OneToOneField(User,on_delete=models.CASCADE)
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
	# relates to sit up scale [60 is excellent 15 is poor] dummies
	# but also to possible 200 situp program so 200 equals maxlevel 150 
	def get_abs_level(self):
		level_abs = self.sit_ups * 0.75
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
		level_back = 0
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
	def save(self, *args, **kwargs):
		graph_initialize, created = ForGraphing.objects.get_or_create(user = self.user, bmi = self.bmi, ibw = self.user_ibw, ibw_hamwi = self.user_ibw_hamwi, current_weight = self.weight_for_calc)
		graph_initialize.save()
		weight_initialize = Weightgraph(user = self.user, weight = self.weight_for_calc)
		weight_initialize.save()
		initial_level = LevelGrowthGraph(user = self.user, abslevel = self.abs_level, leg = self.leg_level, upperarm = self.uarm_level, lowerarm = self.larm_level, back = self.back_level, chest = self.cht_level, glutes = self.glu_level, neck = self.nec_level, overall = self.overall)
		initial_level.save()
		super(Calculations, self).save(*args, **kwargs)
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
	equipment = models.CharField(max_length=200, default="Body Only")
	def __str__(self):
		return self.ex_name
	def grab_exercise(self):
		array = [self.ex_key,self.ex_name,self.ex_type,self.ex_dif]
		return array
#<<< Using exercise key to add
#add exercise from web as long as i have exercise key i can declare Exercise object
# ex = Exercise(ex_key = exercise_key) then use as such
#ExerciseRoutine(user=request.user, exercise = ex)
# then have a form which adds in the remaining fields 
#>>>
class ExerciseRoutine(models.Model):
	user = models.ForeignKey(User , related_name = 'routine',on_delete=models.CASCADE)
	exercise = models.ForeignKey('Exercise', on_delete = models.CASCADE)
	sets = models.IntegerField(default=1, validators = [MinValueValidator(1),MaxValueValidator(100)])
	reps = models.IntegerField(default=1, validators = [MinValueValidator(1),MaxValueValidator(100)])
	weight = models.IntegerField(default=0, validators = [MinValueValidator(0),MaxValueValidator(500)])
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
			the_experience = ((self.sets * self.reps) * 0.75)/100
			if self.exercise.ex_type == 'Stretching':
				the_experience = 0.00455
		return the_experience
	abs_ex = property(absex)
	def legex(self):
		the_experience = 0
		my_profile = Profile.objects.get(user=self.user)
		string = self.exercise.categories
		if 'Abductors' or 'Adductors' or 'Calves' or 'Hamstrings' in string:
			the_experience = ((self.weight +(my_profile.weight * 0.72)) * (self.reps**0.1)) / 150
			if self.exercise.ex_type == 'Stretching':
				the_experience = 0.00455
		return the_experience 
	leg_ex = property(legex)
	def uarmex(self):
		the_experience = 0
		my_profile = Profile.objects.get(user=self.user)
		string = self.exercise.categories
		if 'Biceps' or 'Triceps' in string:
			the_experience = ((self.weight +(my_profile.weight * 0.72)) * (self.reps**0.1)) / 150
			if self.exercise.ex_type == 'Stretching':
				the_experience = 0.00455
		return the_experience 
	uarm_ex = property(uarmex)
	def larmex(self):
		the_experience = 0
		my_profile = Profile.objects.get(user=self.user)
		string = self.exercise.categories
		if 'Forearms' in string:
			the_experience = ((self.weight +(my_profile.weight * 0.72)) * (self.reps**0.1)) / 300
			if self.exercise.ex_type == 'Stretching':
				the_experience = 0.00455
		return the_experience
	larm_ex = property(larmex)
	def backex(self):
		the_experience = 0
		my_profile = Profile.objects.get(user=self.user)
		string = self.exercise.categories
		if 'Lats' or 'Lower' or 'Middle' or 'Traps' in string:
			the_experience = ((self.weight +(my_profile.weight * 0.50)) * (self.reps**0.1)) / 450
			if self.exercise.ex_type == 'Stretching':
				the_experience = 0.00455
		return the_experience
	back_ex = property(backex)
	def chtex(self):
		the_experience = 0
		my_profile = Profile.objects.get(user=self.user)
		string = self.exercise.categories
		if 'Chest' in string:
			the_experience = ((self.weight +(my_profile.weight * 0.72)) * (self.reps**0.1)) / 150
			if self.exercise.ex_type == 'Stretching':
				the_experience = 0.00455
		return the_experience
	cht_ex = property(chtex)
	def gluex(self):
		the_experience = 0
		my_profile = Profile.objects.get(user=self.user)
		string = self.exercise.categories
		if 'Glutes' in string:
			the_experience = ((self.weight +(my_profile.weight * 0.72)) * (self.reps**0.1)) / 150
			if self.exercise.ex_type == 'Stretching':
				the_experience = 0.00455
		return the_experience
	glu_ex = property(gluex)
	def necex(self):
		the_experience = 0
		my_profile = Profile.objects.get(user=self.user)
		string = self.exercise.categories
		if 'Neck' in string:
			the_experience = ((self.weight +(my_profile.weight * 0.45)) * (self.reps**0.1)) / 450
			if self.exercise.ex_type == 'Stretching':
				the_experience = 0.00455
		return the_experience
	nec_ex = property(necex)
	def __str__(self):
		string = "routine"
		return string
	def truedelete(self):
		#self contained method which will update levels based on
		#the exercise complete
		current_levels = LevelGrowthGraph.objects.filter(user=self.user).latest('date')
		new_abs = self.absex() + current_levels.abslevel
		new_leg = self.legex() + current_levels.leg
		new_uarm = self.uarmex() + current_levels.upperarm
		new_larm = self.larmex() + current_levels.lowerarm
		new_back = self.backex() + current_levels.back
		new_chest = self.chtex() + current_levels.chest
		new_glu = self.gluex() + current_levels.glutes
		new_nec = self.necex() + current_levels.neck
		new_overall = (new_abs + new_leg + new_uarm + new_larm + new_back + new_chest + new_glu	+ new_nec) / 8
		month_to_enter = datetime.now().month
		year_to_enter = datetime.now().year
		day_to_enter = datetime.now().day
		new_levels, created = LevelGrowthGraph.objects.get_or_create(user=self.user,month=month_to_enter,day=day_to_enter,year=year_to_enter,abslevel = new_abs, leg = new_leg,upperarm = new_uarm,lowerarm = new_larm,back = new_back,chest = new_chest,glutes = new_glu,neck = new_nec,overall = new_overall)
		new_levels.save()
		super(ExerciseRoutine, self).delete()
	#def delete(self):
	#	x = SecretCalculator.objects.filter(user=self.user).update(abs_ex += self.abs_ex, leg_ex += self.leg_ex, uarm_ex += self.uarm_ex, larm_ex += self.larm_ex, back_ex += self.back_ex, cht_ex += self.cht_ex, glu_ex += self.glu_ex, nec_ex += self.nec_ex)
	#	x.save()
	#	super(ExerciseRoutine, self).delete()
