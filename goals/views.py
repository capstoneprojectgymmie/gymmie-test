from django.shortcuts import get_object_or_404, render
#added froms and imports
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Exercise



# Create your views here.
#so far: Homepage, Meet the Team, Progress Report
def index(request):
    return render_to_response('goals/homepage.html')
def meettheteam(request):
	return render(request, 'goals/MeettheTeam/MeetTheTeam.html')
def progressreport(request):
	return render(request, 'goals/progressreportpage.html')
def exercise(request, exercise_id):
	the_exercise = get_object_or_404(Exercise, ex_key = exercise_id)
	return render(request, 'goals/ex_template.html', {'the_exercise': the_exercise})
