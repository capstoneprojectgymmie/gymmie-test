from django.db import models
#just in case
import csv

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