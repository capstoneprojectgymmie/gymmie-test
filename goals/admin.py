from django.contrib import admin
# get models from models file
from .models import Exercise, Abs, Shoulders, Glutes, Hamstrings, Lower_Back, Lats, Quadriceps, Triceps, Calves, Forearms, Traps, Abductors, Adductors, Middle_Back, Biceps, Chest, Neck

# Register your models here.
admin.site.register(Exercise)
admin.site.register(Abs)
admin.site.register(Shoulders)
admin.site.register(Glutes)
admin.site.register(Hamstrings)
admin.site.register(Lower_Back)
admin.site.register(Lats)
admin.site.register(Quadriceps)
admin.site.register(Triceps)
admin.site.register(Calves)
admin.site.register(Forearms)
admin.site.register(Traps)
admin.site.register(Abductors)
admin.site.register(Adductors)
admin.site.register(Middle_Back)
admin.site.register(Biceps)
admin.site.register(Chest)
admin.site.register(Neck)