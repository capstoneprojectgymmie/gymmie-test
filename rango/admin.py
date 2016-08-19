from django.contrib import admin
from rango.models import (
	Profile,
	Weightgraph,
	Calculations,
	ForGraphing,
	LevelsGraph,
	Exercise,
	ExerciseRoutine
	)
# Register your models here.
admin.site.register(Profile)
admin.site.register(Weightgraph)
admin.site.register(Calculations)
admin.site.register(ForGraphing)
admin.site.register(LevelsGraph)
admin.site.register(Exercise)
admin.site.register(ExerciseRoutine)